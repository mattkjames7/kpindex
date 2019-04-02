import os
from . import Globals

def _DownloadFTPIndex():
	'''
	This routine downloads the index.html of the Potzdam FTP site
	ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/
	
	Returns:
		Boolean, True if index file exists
	
	'''
	#check that the temporary folder exists
	if not os.path.isdir(Globals.DataPath+'tmp/'):
		os.system('mkdir -pv '+Globals.DataPath+'tmp/')

	#download using wget
	os.system('wget ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/ -O '+Globals.DataPath+'tmp/index.html')
	

	#check that the file exists, return True if so
	return os.path.isfile(Globals.DataPath+'tmp/index.html')
	
