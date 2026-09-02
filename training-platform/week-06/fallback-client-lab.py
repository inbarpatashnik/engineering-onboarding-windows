"""Deterministic client-semantics fallback. This is not Kafka integration evidence."""
import hashlib, json

class MemoryLog:
    def __init__(self, partitions=3):
        self.parts=[[] for _ in range(partitions)]; self.commits={}
    def publish(self, key, value):
        p=int.from_bytes(hashlib.sha256(key.encode()).digest()[:4],"big") % len(self.parts)
        offset=len(self.parts[p]); self.parts[p].append((key,value)); return p,offset
    def poll(self, group):
        for p,records in enumerate(self.parts):
            offset=self.commits.get((group,p),0)
            for current in range(offset,len(records)):
                yield p,current,records[current]
    def commit(self, group, partition, next_offset): self.commits[(group,partition)]=next_offset

def main():
    log=MemoryLog(); seen=set(); applied=[]; rejected=[]
    samples=[
      ("resource-1",'{"event_id":"evt-1","version":1}'),
      ("resource-1",'{"event_id":"evt-2","version":1}'),
      ("resource-2",'{broken'),
      ("resource-1",'{"event_id":"evt-2","version":1}')]
    for key,value in samples: print("published",key,log.publish(key,value))
    for p,o,(_,raw) in list(log.poll("student")):
        try:
            event=json.loads(raw)
            if event["version"] != 1: raise ValueError("unsupported version")
            if event["event_id"] not in seen: applied.append(event["event_id"]); seen.add(event["event_id"])
        except (json.JSONDecodeError,KeyError,ValueError) as exc: rejected.append((p,o,str(exc)))
        log.commit("student",p,o+1)
    assert applied == ["evt-1","evt-2"] and len(rejected)==1
    assert list(log.poll("student")) == []
    assert len(list(log.poll("replay"))) == 4
    print("PASS fallback: per-key partitioning, commits, restart, replay, idempotency, and poison handling")
    print("LIMITATION: no real Kafka protocol, acknowledgements, rebalance, retention, or broker failure was tested")
if __name__ == "__main__": main()
