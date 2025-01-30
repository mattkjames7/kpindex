from . import Globals
from ftplib import FTP
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
	"""
	This function is a callback for downloading files over FTP. It writes the received chunks to an open file and updates progress bars.
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
	Write a docstring for the function `_DownloadFTPFile(fname)`.
	
	The function takes two arguments: `addr` and `name`. It uses an FTP client to download the file from the given address, saving it locally. The full path of the downloaded file is returned.
	
	Args:
	    addr (str): The URL or address of the FTP file to be downloaded, e.g., 'ftp://example.com/path/to/file.txt'.
	    fname (str): The name of the file to be saved as.
	
	Returns:
	    str: The full local path where the file was saved.
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
