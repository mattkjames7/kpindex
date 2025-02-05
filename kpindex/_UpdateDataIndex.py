import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	"""
	
	Updates the data index file with the given index data.
	
	Args:
	    idx (numpy.recarray): A numpy recarray containing the file names, time
	resolution, and dates for all data files.
	
	Returns:
	    None
	
	
	"""
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
