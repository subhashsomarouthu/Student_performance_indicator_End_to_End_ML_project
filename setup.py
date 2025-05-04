
from setuptools import setup, find_packages
from pathlib import Path



def get_requirements(file_path: str) -> list:
    """This function returns a list of requirements."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="Student_performance_indicator_End_to_End_ML_project",
    version="0.0.1",
    author="subhash",
    author_email="sspchakravarthy@gmail.com",
    packages=find_packages(),
    package_data={'': ['*.csv', '*.txt', '*.json']},
    install_requires=get_requirements('requirements.txt')
)