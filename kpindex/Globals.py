import os

#try and find the KPDATA_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('KPDATA_PATH')+'/'
except:
	print('Please set KPDATA_PATH environment variable')
	DataPath = ''

dtype = [('Date','int32'),('Index','int8'),('ut0','float32'),('ut1','float32'),
		('Kp','float32'),('Sum','float32'),('Ap','int8'),('Cp','float32'),
		('Activity','U3')]

Data = None
