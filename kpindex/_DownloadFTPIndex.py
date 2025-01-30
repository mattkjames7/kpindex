import os
from . import Globals

def _DownloadFTPIndex(ftp):
	"""
	
	This routine downloads the index.html of the Potzdam FTP site
	
	Args:
	    ftp (obj): The FTP client object used to connect to the server.
	
	Returns:
	    bool: True if index file exists after download, False otherwise.
	
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
	
