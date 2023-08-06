from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='CounterOfVisit',
    version='0.2',
    description='A package to count the number of visits',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Johan Polsinelli',
    author_email='johan.polsinelli@gmail.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
