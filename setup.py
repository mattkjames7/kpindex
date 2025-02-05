import setuptools
from setuptools.command.install import install
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def getversion():
	"""
	
	Reads the version string from the `__init__.py` file located in the
	`kpindex` package.
	
	This function retrieves the version number defined in the `__version__`
	variable by reading the `__init__.py` file of the `kpindex` package. If the
	version cannot be found, it returns 'unknown'.
	
	Returns:
	    str: The version number as a string, or 'unknown' if the version is not
	defined.
	
	"""
	#get the init file path
	thispath = os.path.abspath(os.path.dirname(__file__))+'/'
	initfile = thispath + 'kpindex/__init__.py'
	
	#read the file in
	f = open(initfile,'r')
	lines = f.readlines()
	f.close()
	
	#search for the version
	version = 'unknown'
	for l in lines:
		if '__version__' in l:
			s = l.split('=')
			version = s[-1].strip().strip('"').strip("'")
			break
	return version
	
version = getversion()



setuptools.setup(
    name="kpindex",
    version=version,
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
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
    ],
    install_requires=[
		'numpy',
		'RecarrayTools',
		'PyFileIO',
	],
)



