from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''this function will written a list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        HYPEN_E_DOT = '-e .'


        if HYPEN_E_DOT in  requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
name = 'MLPROJECT',
version = '0.01',
author = 'jayesh',
author_email = 'jayeshsinh.msismpl2024@learner.manipal.edu',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)