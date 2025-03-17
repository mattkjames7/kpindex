import numpy as np
import PyFileIO as pf
from . import Globals
import DateTimeTools as TT

def _ReadKpTxt(fname):
    

	#read in the ascii
	lines = pf.ReadASCIIFile(fname)
	nl = lines.size

	#remove lines with comments
	lines = np.array([line.strip() for line in lines if not line.startswith("#")])


	#temp dtype
	dtype0 = [	('Year','int32'),
	   			('Month','int32'),
				('Day','int32'),
				('ut0','float32'),
				('utm','float32'),
				('days','float32'),
				('daysm','float32'),
				('Kp','float32'),
				('Ap','int32'),
				('D','int8'),]

	# list the columns to map to the new dtype
	cols = ["Year","Month","Day","ut0","utm","days","daysm","Kp","Ap","D"]
	
	# read data into recarray
	dataraw = pf.ReadASCIIData(lines,Header=False)
	data = np.recarray(dataraw.size,dtype=dtype0)
	for i,col in enumerate(cols):
		data[col] = dataraw[f"Col{i:02d}"]

	#get the output data
	out = np.recarray(dataraw.size,dtype=Globals.dtype)

	out.Date = TT.DateJoin(data.Year,data.Month,data.Day)
	out.ut0 = data.ut0
	out.ut1 = out.ut0 + 3.0
	out.utm = data.utm
	out.utc = TT.ContUT(out.Date,out.utm)
	out.Kp = data.Kp
	out.Ap = data.Ap
	out.D = data.D

	# correct bad values of Kp
	out.Kp[out.Kp < 0] = np.nan

	return out
