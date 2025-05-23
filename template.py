import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Plant_class"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

def create_file_structure(files_list):
    for file_path in files_list:
        # Get the directory path
        dir_path = Path(file_path).parent

        # Check if the directory exists, if not create it
        if not dir_path.exists():
            logging.info(f"Creating directory: {dir_path}")
            dir_path.mkdir(parents=True, exist_ok=True)

        # Create the file (if it does not exist)
        if not Path(file_path).exists():
            logging.info(f"Creating file: {file_path}")
            with open(file_path, 'w') as file:
                # You can add initial content to files if required, for now leaving them empty
                pass

if __name__ == "__main__":
    logging.info(f"Starting to create project structure for {project_name}")
    create_file_structure(list_of_files)
    logging.info(f"Project structure for {project_name} created successfully.")
