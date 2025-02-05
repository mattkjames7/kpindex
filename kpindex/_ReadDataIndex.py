import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ReadDataIndex():
        """
        Reads an index file containing the file names, update dates, and
resolutions.

            This function checks for the existence of a specific index file. If
the file exists, it is read to extract relevant data. If the file does not
exist, an empty record array is returned.

            Returns:
                numpy.recarray: A record array containing file names, old file
names, and update dates if the index file exists; otherwise, an empty record
array.
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
