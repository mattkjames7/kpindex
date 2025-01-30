import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	"""
	This function updates the data index file.
	
	    Args:
	        idx (numpy.recarray): A numpy array containing file names, time resolution,
	        and dates for all data files.
	
	    Returns:
	        None: This function does not return anything.
	
	    Note:
	        The DataPath must be defined in the globals dictionary.
	"""
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
