import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/_init_.py",
   f"src/{package_name}/_init_.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/_init_.py",
   "tests/unit/_init_.py",
   "tests/integration/_init_.py",
   "init_setup.sh",
   "requirements.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated