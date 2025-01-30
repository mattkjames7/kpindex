from . import Globals
from ftplib import FTP
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
	"""
	This function defines a callback for downloading files via FTP. It writes chunks of the file to an open binary file and updates a progress bar with ASCII characters.
	"""
	#get the size of the file
	#size = ftp.size(Globals.ftpdir+fname)
	size = ftp.size(fname)
	
	#set progress to 0
	global progress
	progress = 0
	
	def callback(chunk):
		f.write(chunk)
		global progress
		progress += len(chunk)
		
		ndone = np.int32(np.ceil(50*progress/size))
		sdone = '\r[' + '='*ndone + '-'*(50-ndone) + ']'
		print(sdone,end='')
		
	return callback


def _DownloadFTPFile(fname):
	"""
	This function is responsible for downloading a file from an FTP server. It establishes a connection, downloads the file, and returns the full path of the downloaded file on the local machine.
	
	Args:
	    addr (str): The full address of the FTP file to download, e.g., ftp://example.com/path/to/file.txt.
	    fname (str): The name of the file to be downloaded.
	
	Returns:
	    str: The full path to the downloaded file on the local machine.
	"""

	#login to the FTP server
	ftp = FTP(Globals.ftpbase)
	ftp.login()  
	ftp.cwd(Globals.ftpdir)

	#open the output file
	f = open(Globals.DataPath+'tmp/'+fname,"wb")	
	
	#get the callback function
	cb = _GetCallback(f,ftp,fname)
	
	#download binary file using ftplib
	ftp.retrbinary('RETR '+fname, cb)
	print()
	
	#close the file
	f.close()
	
	#close FTP connection
	ftp.close()
	
	#return the file name
	return Globals.DataPath+'tmp/'+fname
