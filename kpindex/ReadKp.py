from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
	"""
	Read the converted Kp data for a specified year.
	
	    Args:
	        Year (int): The year for which the Kp data is to be read, specified
	in the format yyyy.
	
	    Returns:
	        numpy.recarray: A record array containing the Kp data for the
	specified year. If the file does not exist, returns an empty record array
	with the specified dtype.
	"""
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
