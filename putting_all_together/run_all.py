from pathlib import Path
import subprocess
import sys

this_dir = Path(__file__).parent
for f in this_dir.glob("chap*.py"):
    cmd = [sys.executable, str(f), 'low']
    print(f"Running {f.name}")
    subprocess.run(cmd, check=True)