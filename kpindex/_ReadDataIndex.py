import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ReadDataIndex():
	"""
	Reads an index file containing the file names, update dates and resolutions.
	
	    Args:
	        None. This function does not take any parameters.
	
	    Returns:
	        np.recarray: The contents of the DataIndex.dat file as a structured numpy array.
	"""
	#define the datatype
	dtype = [('FileName','object'),('OldFileName','object'),('UpdateDate','object')]
	
	#check if the index file exists
	fname = Globals.DataPath+'DataIndex.dat'
	if not os.path.isfile(fname):
		return np.recarray(0,dtype=dtype)
		
	#if it does exist, then read it
	data = pf.ReadASCIIData(fname,Header=True,dtype=dtype)

	return data
