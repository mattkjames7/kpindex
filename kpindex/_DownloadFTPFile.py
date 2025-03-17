from . import Globals
from ftplib import FTP
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
	'''
	callback function for downloading the file
	
	Inputs
	======
	f : file
		instance of an open file (binary)
	ftp : FTP()
		ftp instance
	fname : str
		Name of the file on the server
	
	'''
	# Switch to binary mode before making SIZE call
	ftp.voidcmd("TYPE I")

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


def _DownloadFTPFile(fname,retries=3):
	'''
	Downloads a file from an FTP site, returns the full path of the 
	local version of that file.
	
	Inputs:
		addr: full address of file to be downloaded e.g. 
			ftp://a.b.c/folder/file.txt
		fname: file name e.g. file.txt
		
	Returns:
		full path to downloaded file
	'''

	#login to the FTP server
	ftp = FTP(Globals.ftpbase, timeout=10)
	ftp.login()  
	ftp.cwd(Globals.ftpdir)

	#open the output file
	f = open(f"{Globals.DataPath}/tmp/{fname}","wb")	
	
	#get the callback function
	cb = _GetCallback(f,ftp,fname)
	
	#download binary file using ftplib
	success = False
	for i in range(0,retries):
		try:
			ftp.retrbinary('RETR '+fname, cb)
			success = True
			break
		except:
			print(f"Timeout downloading {fname} (attempt {i+1} of {retries})")
	if not success:
		print(f"Failed to download {fname} {retries} times")
		raise TimeoutError
	print()
	
	#close the file
	f.close()
	
	#close FTP connection
	ftp.close()
	
	#return the file name
	return f"{Globals.DataPath}/tmp/{fname}"
