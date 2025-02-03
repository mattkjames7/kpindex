import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ReadDataIndex():
	"""
	Reads an index file containing the file names, update dates, and resolutions.
	
	    This function checks for the existence of an index file at a specified data path. If the file exists, it reads the content into a structured NumPy array with fields for file names, old file names, and update dates. If the index file does not exist, it returns an empty record array.
	
	    Returns:
	        numpy.recarray: A structured array containing the file names, old file names, and update dates if the index file exists, otherwise an empty record array.
	
	    Raises:
	        FileNotFoundError: If the specified data path does not exist (if applicable).
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
