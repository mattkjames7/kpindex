import numpy as np
from . import Globals
from .ReadKp import ReadKp
import RecarrayTools as RT
from ._ReadDataIndex import _ReadDataIndex

def GetKp(Date=None):
	'''
	Retrieves Kp data from memory, or from file if it hasn't been 
	loaded yet.
	
	Inputs:
		Date: Integer date in the format yyyymmdd, or two element integer
			dates for loading a range of dates.

			
	Returns:
		numpy.recarray
	'''

	#check if the data are loded in memory already
	if Globals.Data is None:
		#read the index to get the full list of files
		idx = _ReadDataIndex()
		YM = np.array([np.int32(x[3:9]) for x in idx.FileName])
		srt = np.argsort(YM)
		YM = YM[srt]
		fnames = idx.FileName[srt]
		
		#read the first integer from each file to find the total number
		# of records
		nf = YM.size
		n = 0
		for i in range(0,nf):
			f = open(Globals.DataPath+'bin/'+fnames[i],'rb')
			tmp = np.fromfile(f,dtype='int32',count=1)[0]
			f.close()
			n += tmp

		#create new output data array
		dtype = Globals.dtype
		data = np.recarray(n,dtype=dtype)
		
		#read data in
		p = 0
		for i in range(0,nf):
			print('\rReading Data {:6.2f}%'.format(100.0*(i+1)/nf),end='')
			tmp = ReadKp(YM[i])
			data[p:p+tmp.size] = tmp
			p += tmp.size
		print()
		
		Globals.Data = data
	
	#see if we need to select a specific data/date range
	if Date is None:
		#return everything
		return Globals.Data
	elif np.size(Date) == 1:
		#a specific date
		use = np.where(Globals.Data.Date == Date)[0]
		return Globals.Data[use]
	else:
		#a range of dates
		use = np.where((Globals.Data.Date >= Date[0]) & (Globals.Data.Date <= Date[1]))[0]
		return Globals.Data[use]
