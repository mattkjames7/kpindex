from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
	"""
	Read Kp data for a given year. The function reads the converted Kp data from a binary file and returns it as a numpy recarray.
	
	Args:
	    Year (int): The year for which to read the Kp data.
	"""
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
