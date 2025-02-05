import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	"""
	
	Updates the data index file.
	
	Args:
	    idx (numpy.recarray): A record array containing the file names, time resolution, and dates for all data files.
	
	
	"""
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
