import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	"""
	This function updates the data index file. It writes new data into an existing data index file if it exists, or creates a new one if it doesn't exist. The input is a numpy.recarray containing filenames, time resolution, and dates for all data files.
	
	Args:
	    idx (numpy.recarray): A numpy array that contains the necessary information to update the data index file.
	"""
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
