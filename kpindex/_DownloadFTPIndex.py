import os
from . import Globals

def _DownloadFTPIndex(ftp):
	"""
	
	Downloads the index.html file from the Potsdam FTP site.
	
	This function connects to an FTP server to retrieve the index.html file
	located at
	ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/. It ensures that the
	temporary
	directory for storing the file exists, and if not, it creates the directory
	before
	downloading the file.
	
	Args:
	    ftp (ftplib.FTP): An active ftplib.FTP connection to the FTP server.
	
	Returns:
	    bool: True if the index.html file exists after the download, False
	otherwise.
	
	
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
	
