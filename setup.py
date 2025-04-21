from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservations",
    version="1.0",
    author="Huy Huynh",
    packages=find_packages(),
    install_requires=requirements,
)