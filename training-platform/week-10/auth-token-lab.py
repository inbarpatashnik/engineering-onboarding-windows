from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from pathlib import Path
import json, tempfile, uuid

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from jwt.algorithms import RSAAlgorithm

ISSUER="https://issuer.training.invalid"
AUDIENCE="training-resource-api"

def paths(directory: Path):
    return directory/"current.json", directory/"jwks.json"

def create_key(directory: Path, kid: str):
    directory.mkdir(parents=True,exist_ok=True)
    key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    private=key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
    (directory/f"{kid}-private.pem").write_bytes(private)
    jwk=json.loads(RSAAlgorithm.to_jwk(key.public_key())); jwk.update({"kid":kid,"use":"sig","alg":"RS256"})
    return jwk

def initialize(directory: Path):
    current,jwks=paths(directory); kid="training-key-1"; jwk=create_key(directory,kid)
    current.write_text(json.dumps({"kid":kid},indent=2),encoding="utf-8")
    jwks.write_text(json.dumps({"keys":[jwk]},indent=2),encoding="utf-8")

def rotate(directory: Path):
    current,jwks=paths(directory); data=json.loads(jwks.read_text(encoding="utf-8"))
    kid=f"training-key-{len(data['keys'])+1}"; data["keys"].append(create_key(directory,kid))
    current.write_text(json.dumps({"kid":kid},indent=2),encoding="utf-8")
    jwks.write_text(json.dumps(data,indent=2),encoding="utf-8"); return kid

def issue(directory: Path, subject: str, scope: str, lifetime: int, issuer: str, audience: str):
    current,_=paths(directory); kid=json.loads(current.read_text(encoding="utf-8"))["kid"]
    key=(directory/f"{kid}-private.pem").read_bytes(); now=datetime.now(timezone.utc)
    claims={"iss":issuer,"aud":audience,"sub":subject,"scope":scope,"iat":now,"nbf":now,"exp":now+timedelta(seconds=lifetime),"jti":str(uuid.uuid4())}
    return jwt.encode(claims,key,algorithm="RS256",headers={"kid":kid,"typ":"at+jwt"})

def verify(directory: Path, token: str, required_scope: str=""):
    header=jwt.get_unverified_header(token)
    if header.get("typ") != "at+jwt": raise ValueError("wrong token type")
    if header.get("alg") != "RS256": raise ValueError("disallowed algorithm")
    jwks=json.loads(paths(directory)[1].read_text(encoding="utf-8"))
    match=[k for k in jwks["keys"] if k.get("kid")==header.get("kid")]
    if len(match)!=1: raise ValueError("unknown or ambiguous key id")
    key=RSAAlgorithm.from_jwk(json.dumps(match[0]))
    claims=jwt.decode(token,key,algorithms=["RS256"],issuer=ISSUER,audience=AUDIENCE,options={"require":["exp","iat","nbf","iss","aud","sub"]})
    scopes=set(claims.get("scope","").split())
    if required_scope and required_scope not in scopes: raise PermissionError("authenticated but missing required scope")
    return claims

def self_test():
    with tempfile.TemporaryDirectory() as raw:
        directory=Path(raw); initialize(directory)
        valid=issue(directory,"service-a","resources:read",300,ISSUER,AUDIENCE)
        assert verify(directory,valid,"resources:read")["sub"]=="service-a"
        try: verify(directory,issue(directory,"service-a","",300,ISSUER,"wrong-api"))
        except jwt.InvalidAudienceError: pass
        else: raise AssertionError("wrong audience was accepted")
        old=valid; rotate(directory); assert verify(directory,old)["sub"]=="service-a"
        try: verify(directory,issue(directory,"service-a","",-1,ISSUER,AUDIENCE))
        except jwt.ExpiredSignatureError: pass
        else: raise AssertionError("expired token was accepted")
    print("PASS: signature, claims, audience, expiry, scope, and rotation overlap")

def main():
    parser=ArgumentParser(); sub=parser.add_subparsers(dest="command",required=True)
    for name in ("init","rotate"):
        p=sub.add_parser(name); p.add_argument("--directory",type=Path,required=True)
    p=sub.add_parser("issue"); p.add_argument("--directory",type=Path,required=True); p.add_argument("--subject",required=True); p.add_argument("--scope",default=""); p.add_argument("--lifetime",type=int,default=300); p.add_argument("--issuer",default=ISSUER); p.add_argument("--audience",default=AUDIENCE); p.add_argument("--output",type=Path,required=True)
    p=sub.add_parser("verify"); p.add_argument("--directory",type=Path,required=True); p.add_argument("--token-file",type=Path,required=True); p.add_argument("--required-scope",default="")
    sub.add_parser("self-test"); args=parser.parse_args()
    if args.command=="init": initialize(args.directory); print(args.directory)
    elif args.command=="rotate": print(rotate(args.directory))
    elif args.command=="issue": args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(issue(args.directory,args.subject,args.scope,args.lifetime,args.issuer,args.audience),encoding="utf-8"); print(args.output)
    elif args.command=="verify": print(json.dumps(verify(args.directory,args.token_file.read_text(encoding="utf-8").strip(),args.required_scope),indent=2))
    else: self_test()
if __name__=="__main__": main()
