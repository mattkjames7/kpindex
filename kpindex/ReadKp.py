from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(YearMonth):
	'''
	Read in the converted Kp data for one month.
	
	Inputs:
		Year: integer year*100 + Month (yyyymm).
		
	Returns: 
		numpy.recarray
	'''
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:6d}.bin'.format(YearMonth)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
