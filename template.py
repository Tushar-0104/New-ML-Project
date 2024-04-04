import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
project_name="mlproject"
list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_trainer.py",
    f"src/{project_name}/components/data_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    
]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir!=" ":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory{filedir} for the file{filename}")
    if(not os.path.exists(file_path)):
        with open(file_path,'w') as f:
            logging.info(f"Creating empty file:{file_path}")
    else:
         logging.info(f"{file_path} is already exist")
