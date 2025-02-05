from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
	"""
	Read in the converted Kp data for one year.
	
	Args:
	    Year (int): The year (yyyy) for which Kp data is to be read.
	
	Returns:
	    numpy.recarray: A record array containing the Kp data for the specified year, or an empty record array if the file is not found.
	"""
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
