from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadKp(Year):
    """
    Reads in the converted Kp data for a specific year.
    
    Args:
        Year (int): The year for which to read Kp data (e.g., 2023).
    
    Returns:
        numpy.recarray: A NumPy record array containing the Kp data for the specified year, or an empty array if the file is not found.
    """
	dtype = Globals.dtype
		
	fname = Globals.DataPath+'bin/'+'Kp-{:04d}.bin'.format(Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)