from . import Globals
from ftplib import FTP
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
	"""
	
	Callback function for downloading a file from an FTP server.
	
	This function creates a callback that writes chunks of data to a provided open file object
	while also updating and displaying the download progress in the console.
	
	Args:
	    f (file): An open file object in binary mode where the downloaded content will be written.
	    ftp (FTP): An instance of an FTP connection to interact with the server.
	    fname (str): The name of the file on the FTP server that is being downloaded.
	
	Returns:
	    function: A callback function that writes chunks of data to the file and displays progress.
	
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
	
	Downloads a file from an FTP site and returns the full path of the 
	local version of that file.
	
	Args:
	    fname (str): The file name to be downloaded, e.g., 'file.txt'.
	
	Returns:
	    str: The full path to the downloaded file.
	
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
