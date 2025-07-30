from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    This function reads the requirements file and returns a list of packages.
    """
    requirements = []
    # Read the requirements file
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  

    # Remove any -e . entry if present
    # This is used for local development
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    # Return the list of requirements  
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kushal Kharel',
    author_email='kushalkharelsearch@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn', 'scikit-learn'],
    install_requires=get_requirements('requirements.txt'),
)