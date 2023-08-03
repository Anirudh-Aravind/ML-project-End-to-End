from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ML Project",
    version='0.0.1',
    author='Anirudh-Aravind',
    author_email='anirudhparavind@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')    
)