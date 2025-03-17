import os
from . import Globals

def _DownloadFTPIndex(ftp):
	'''
	This routine downloads the index.html of the Potzdam FTP site
	ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/
	
	Returns:
		Boolean, True if index file exists
	
	'''
	#check that the temporary folder exists
	if not os.path.isdir(f"{Globals.DataPath}/tmp"):
		os.makedirs(f"{Globals.DataPath}/tmp")

	#download using ftplib
	foo=open(f"{Globals.DataPath}/tmp/index.html","w")	
	def customWriter(line):
		foo.write(line + "\n")

	ftp.retrlines('LIST', customWriter)
	foo.close()
	

	#check that the file exists, return True if so
	return os.path.isfile(f"{Globals.DataPath}/tmp/index.html")
	
