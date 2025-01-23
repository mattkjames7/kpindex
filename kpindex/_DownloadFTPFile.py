from . import Globals
from ftplib import FTP
progress = 0
import numpy as np

def _GetCallback(f,ftp,fname):
    """
    Generate a callback function for downloading files using FTP. 
    
    Args:
        f (file): An open file instance in binary mode to write the downloaded data.
        ftp (FTP()): An active FTP instance.
        fname (str): The name of the file on the server.
    
    Returns:
        callback(chunk): A function that writes chunks of data to the given file and prints a progress bar during the download process. 
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
    
        Downloads a file from an FTP site, returns the full path of the 
    local version of that file.
    
        Args:
            fname (str): The name of the file to download from the FTP server.
    
        Returns:
            str: The full path to the downloaded file in the 'tmp' directory within Globals.DataPath.
        
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