import os
from . import Globals

def _DownloadFTPIndex(ftp):
        """
        Downloads the index.html file from the Potsdam FTP site.

        This function retrieves the index.html file from the specified FTP
location at
        ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/. It checks if the
temporary
        directory exists and creates it if not. The actual download is performed
using
        ftplib's retrieving methods.

        Args:
            ftp (ftplib.FTP): An FTP connection object to connect to the FTP
site.

        Returns:
            bool: True if the index file was successfully downloaded and exists,
            otherwise False.
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
	
