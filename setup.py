# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-schase15", # the name that you will install via pip
    version="1.0",
    author="Steven Chase",
    author_email="schase15@email.com",
    description="First time creating a package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/schase15/lambdata-schase15",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)