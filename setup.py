from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e.'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n"," ") for i in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

setup(
    name = 'Music Genre Classification Web App',
    version = '1.0.0',
    author = 'Bhavya Prakash',
    author_email = 'bhavyaprakash2002@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)