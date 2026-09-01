import subprocess, sys, tempfile, unittest
from pathlib import Path
SCRIPT=Path(__file__).parents[1]/"python"/"build_week01_git_lab.py"
class Week01GitLabTests(unittest.TestCase):
    def test_fixture_has_regression_and_branches(self):
        with tempfile.TemporaryDirectory() as d:
            repo=Path(d)/"lab"
            subprocess.run([sys.executable,str(SCRIPT),"--output",str(repo)],check=True,capture_output=True,text=True)
            failed=subprocess.run([sys.executable,"verify.py"],cwd=repo,capture_output=True,text=True)
            self.assertNotEqual(failed.returncode,0)
            branches=subprocess.run(["git","branch","--format=%(refname:short)"],cwd=repo,check=True,capture_output=True,text=True).stdout
            self.assertIn("conflict-left",branches); self.assertIn("conflict-right",branches); self.assertIn("messy-history",branches)
            tags=subprocess.run(["git","tag"],cwd=repo,check=True,capture_output=True,text=True).stdout
            self.assertIn("known-good",tags)
            subprocess.run(["git","checkout","conflict-right"],cwd=repo,check=True,capture_output=True,text=True)
            conflict=subprocess.run(["git","merge","conflict-left"],cwd=repo,capture_output=True,text=True)
            self.assertNotEqual(conflict.returncode,0)
            subprocess.run(["git","merge","--abort"],cwd=repo,check=True,capture_output=True,text=True)
if __name__ == "__main__": unittest.main()
