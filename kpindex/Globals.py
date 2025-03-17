import os

#try and find the KPDATA_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)

DataPath = os.getenv('KPDATA_PATH')
if not DataPath:
	DataPath = f"{os.getenv('HOME')}/kpdata"
	if not os.path.isdir(DataPath):
		print(f"$KPDATA_PATH not set, creating: {DataPath}")
		print('Please set KPDATA_PATH environment variable to use a different path')
		os.makedirs(DataPath)

ftpbase = 'ftp.gfz-potsdam.de'
#ftpdir = 'pub/home/obs/kp-ap/tab/'
ftpdir = 'pub/home/obs/Kp_ap_Ap_SN_F107/'
#ftpadress = 'ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/'
ftpadress = 'ftp://ftp.gfz-potsdam.de/pub/home/obs/Kp_ap_Ap_SN_F107/'

dtype = [	('Date','int32'),
	 		('ut0','float32'),
			('ut1','float32'),
			('utm','float32'),
			('utc','float32'),
			('Kp','float32'),
			('Ap','int32'),
			('D','int8')]

Data = None
