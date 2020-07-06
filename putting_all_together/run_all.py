''' just a quick check with low res image of all these to see that they 
still run'''

from pathlib import Path
import subprocess
import sys


this_dir = Path(__file__).parent
for f in this_dir.glob("chap*.py"):
    cmd = [sys.executable, str(f), 'low']
    print(f"Running {f.name}")
    subprocess.run(cmd, check=True)

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
