import numpy as np
import PyFileIO as pf
from . import Globals
import DateTimeTools as TT

def _ReadKpTxt(fname):
    

	"""
	Reading Kp and Ap data from a text file.
	
	This function reads an ASCII file that contains Kp and Ap values along with their respective dates and times. It filters out any lines that contain comments, structures the data into a specific format, and returns it as a structured NumPy record array.
	
	Args:
	    fname (str): The name of the ASCII file to read.
	
	Returns:
	    np.recarray: A structured array containing the parsed data with fields for Date, ut0, ut1, utm, utc, Kp, Ap, and D.
	"""
	#read in the ascii
	lines = pf.ReadASCIIFile(fname)
	nl = lines.size

	#remove lines with comments
	good = np.zeros(nl,dtype='bool')
	for i in range(0,nl):
		if not '#' in lines[i]:
			good[i] = True
	use = np.where(good)[0]
	lines = lines[use]

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
	data = pf.ReadASCIIData(lines,Header=False,dtype=dtype0)

	#get the output data
	out = np.recarray(data.size,dtype=Globals.dtype)

	out.Date = TT.DateJoin(data.Year,data.Month,data.Day)
	out.ut0 = data.ut0
	out.ut1 = out.ut0 + 3.0
	out.utm = data.utm
	out.utc = TT.ContUT(out.Date,out.utm)
	out.Kp = data.Kp
	out.Ap = data.Ap
	out.D = data.D

	return out
