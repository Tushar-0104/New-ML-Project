from typing import List
from setuptools import setup,find_packages
setup(
    name="ml project",
    version="0.1",
    author="Tushar Sharma",
    author_email="tusharsharma7024@gmail.com",
    packages=find_packages(),
    get_requirements=('requirements.txt') 

)

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n'," ") for req in requirements]
        return requirements
    


