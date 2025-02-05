import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ReadDataIndex():
	"""
	Reads an index file containing file names, update dates, and resolutions.
	
	    This function checks for the existence of an index file at a predefined
	path. If the file exists, it reads the data into a structured numpy array.
	If the file does not exist, it returns an empty record array with the
	defined data types.
	
	    Returns:
	        np.recarray: A record array containing the data from the index file,
	or an empty record array if the file does not exist.
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
