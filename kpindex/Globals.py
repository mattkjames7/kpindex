import os

#try and find the KPDATA_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('KPDATA_PATH')+'/'
except:
	print('Please set KPDATA_PATH environment variable')
	DataPath = ''

ftpbase = 'ftp.gfz-potsdam.de'
ftpdir = 'pub/home/obs/kp-ap/tab/'
ftpadress = 'ftp://ftp.gfz-potsdam.de/pub/home/obs/kp-ap/tab/'

dtype = [('Date','int32'),('Index','int8'),('ut0','float32'),('ut1','float32'),
		('Kp','float32'),('Sum','float32'),('Ap','int8'),('Cp','float32'),
		('Activity','U3')]

Data = None
