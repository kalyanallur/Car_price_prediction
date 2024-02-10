from setuptools import find_packages, setup


def get_requirements(file):
    read = open(file , "r") 
    packages = read.readlines()
    packages = [name.strip() for name in packages]
    if "-e ." in packages:
        packages.remove("-e .")
    return packages

setup(name = "cars price",
      version="0.0.1",
      author="kalyan", 
      packages=find_packages(),
      install_requirements=get_requirements("requirements.txt"))


