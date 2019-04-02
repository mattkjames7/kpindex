import setuptools
from setuptools.command.install import install
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kpindex",
    version="0.0.1",
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="Very simple package for obtaining the kp index data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/kpindex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    install_requires=[
		'numpy',
		'RecarrayTools',
		'PyFileIO',
	],
)



