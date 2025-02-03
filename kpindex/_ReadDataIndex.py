import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ReadDataIndex():
	"""
	
	Reads an index file containing the file names, update dates, and resolutions.
	
	This function checks for the existence of a data index file. If the file is found, it reads the file's contents into a structured NumPy array with predefined datatypes. If the file does not exist, it returns an empty record array.
	
	Returns:
	    numpy.recarray: A record array containing the file names, old file names, and update dates, or an empty record array if the file does not exist.
	
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
