from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
    # Filter out any lines that aren't valid package specifications
    requirements = [req for req in requirements if req and not req.startswith('-e')]
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Harsh',
    author_email='bhardwajanshul28@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

