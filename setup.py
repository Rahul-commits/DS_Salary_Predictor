from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="DS_Salary_predictor",
    version='0.0.1',
    author='Rahul',
    author_email='rahul.narramaneni@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)