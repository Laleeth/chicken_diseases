import os  
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="chicken_diseases"

folder_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #init file is constructor file.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/train.ipynb"
]

for filepath in folder_files:
    filepath =Path(filepath) # forward slash will be in linux but windows accepts backward so we using Path inorder to avoid errors.
    filedir,filename=os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating the directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating the empty file: {filepath}")

    else:
        logging.info(f"{filename} already exist.")


