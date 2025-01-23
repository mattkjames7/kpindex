import numpy as np
from ftplib import FTP
from . import Globals
from ._ReadDataIndex import _ReadDataIndex
from ._DownloadFTPIndex import _DownloadFTPIndex
from ._ParseFTP import _ParseFTP
from ._CompareUpdates import _CompareUpdates
from ._DownloadFTPFile import _DownloadFTPFile
from ._ConvertFTPFile import _ConvertFTPFile
from ._DeleteFTPFile import _DeleteFTPFile

def UpdateLocalData(Force=False):
    """
    Downloads and converts any missing Kp data from the FTP server to the local archive.
    
    Args:
        Force (bool, optional): If True, downloads all files regardless of update dates. Defaults to False.
    
    Returns:
        None:
    """
	
	ftp = FTP(Globals.ftpbase)
	ftp.login()  
	ftp.cwd(Globals.ftpdir)

	#let's download and read the FTP index
	status = _DownloadFTPIndex(ftp)

	if not status:
		print('Download failed; check for write permission to data folder')
		ftp.close()
		return
	FileNames,Addresses,UpdateDates = _ParseFTP()
	
	n = np.size(FileNames)
	ftp.close()
	#check current data index
	idx = _ReadDataIndex()
	
	#now compare update dates
	if Force:
		update = np.ones(n,dtype='bool')
	else:
		update = _CompareUpdates(UpdateDates,FileNames,idx)
	use = np.where(update)[0]
	FileNames = FileNames[use]
	Addresses = Addresses[use]
	UpdateDates = UpdateDates[use]
	n = use.size

	if n == 0:
		print('No files to update.')
		
		return 
		
	for i in range(0,n):
		print('Downloading file {0} of {1}'.format(i+1,n))
		#download file
		tmp = _DownloadFTPFile(FileNames[i])
		
		print('Converting to binary')
		#convert file
		_ConvertFTPFile(tmp,FileNames[i],UpdateDates[i])
		
		#delete text file
		_DeleteFTPFile(tmp)
		
	ftp.close()
	print('Done')	
