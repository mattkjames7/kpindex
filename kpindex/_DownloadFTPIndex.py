import os
from . import Globals

def _DownloadFTPIndex(ftp):
	"""
	This function downloads the index.html from a specified FTP location. It checks if the temporary folder exists and creates it if necessary. Then, it uses ftplib to download the index file into this temporary location. Finally, it verifies that the downloaded file exists and returns its existence as a boolean.
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
	
