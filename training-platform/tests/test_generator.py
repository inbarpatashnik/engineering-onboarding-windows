import json, subprocess, sys, tempfile, unittest
from pathlib import Path
SCRIPT=Path(__file__).parents[1]/"python"/"generate_training_data.py"
class GeneratorTests(unittest.TestCase):
    def test_deterministic_and_valid(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/"a.json",Path(d)/"b.json"
            for p in (a,b): subprocess.run([sys.executable,str(SCRIPT),"--week","6","--output",str(p)],check=True,capture_output=True)
            self.assertEqual(a.read_bytes(),b.read_bytes())
            self.assertEqual(json.loads(a.read_text())["week"],6)
if __name__ == "__main__": unittest.main()
