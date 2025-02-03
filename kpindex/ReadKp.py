from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
	"""
	
	Read in the converted Kp data for one year.
	
	Args:
	    Year (int): The year (yyyy) for which to read the Kp data.
	
	Returns:
	    numpy.recarray: The converted Kp data for the specified year.
	    If the file is not found, an empty numpy.recarray with the defined dtype is returned.
	
	"""
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
