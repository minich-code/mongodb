import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "main.py",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

# Loop through each file path
for filepath in list_of_files:
    # Convert to Path object for easier manipulation
    filepath = Path(filepath) 
    #  Split the file path into directory and file name 
    filedir, filename = os.path.split(filepath) 
    
    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create an empty file if it doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file