import os
from . import Globals

def _DownloadFTPIndex(ftp):
	"""
	
	Downloads the index.html file of the Potsdam FTP site.
	
	This function checks for the existence of a specified temporary directory.
	If the directory does not exist, it creates the directory. Then, it downloads
	the index.html from the specified FTP site and saves it locally. Finally,
	it checks if the index.html file exists and returns a boolean value accordingly.
	
	Args:
	    ftp (ftplib.FTP): An instance of the FTP class from the ftplib module for
	                       connecting to the FTP server.
	
	Returns:
	    bool: True if the index.html file exists in the temporary directory, False otherwise.
	
	"""
	#check that the temporary folder exists
	if not os.path.isdir(Globals.DataPath+'tmp/'):
		os.makedirs(os.path.dirname(Globals.DataPath+'tmp/'))

	#download using ftplib
	foo=open(Globals.DataPath+'tmp/index.html',"w")	
	def customWriter(line):
		foo.write(line + "\n")

	ftp.retrlines('LIST', customWriter)
	foo.close()
	

	#check that the file exists, return True if so
	return os.path.isfile(Globals.DataPath+'tmp/index.html')
	
