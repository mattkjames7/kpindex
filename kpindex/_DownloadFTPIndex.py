import os
from . import Globals

def _DownloadFTPIndex(ftp):
	"""
	
	Downloads the index.html file from the Potsdam FTP site.
	
	This routine retrieves the index file from the specified FTP location and saves it in a temporary directory. It checks for the existence of the temporary folder and creates it if necessary. The function returns a boolean indicating whether the index file was successfully downloaded.
	
	Args:
	    ftp (ftplib.FTP): An instance of FTP class for interacting with the FTP server.
	
	Returns:
	    bool: True if the index file exists after the download attempt, otherwise False.
	
	
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
	
