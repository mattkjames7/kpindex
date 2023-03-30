from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
	'''
	Read in the converted Kp data for one yeah.
	
	Inputs: int
		Year yyyy.
		
	Returns: 
		numpy.recarray
	'''
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)
