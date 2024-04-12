from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "mongodbpkg"
PKG_NAME = "mongo-database-connect"
AUTHOR_USER_NAME = "Minich"
AUTHOR_EMAIL = "minichworks@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with a database.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected content type
    url=f"https://github.com/minich-code/mongodbpkg",
    project_urls={
        "Bug Tracker": f"https://github.com/minich-code/mongodbpkg/issues",
        "Source Code": f"https://github.com/minich-code/mongodbpkg", 
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )