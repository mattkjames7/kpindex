import os
from . import Globals

def _DownloadFTPIndex(ftp):
    """
    Downloads the index.html file from the specified FTP server. 
    
    Args:
    	ftp (ftplib.FTP): An active FTP connection object.
    
    Returns:
    	bool: True if the index.html file was successfully downloaded, False otherwise.
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
