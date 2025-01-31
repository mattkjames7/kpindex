import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	"""
	This function updates the data index file by writing new data to it. The input is a numpy.recarray containing file names, time resolution and dates for all data files. The function then writes this data to DataIndex.dat file located in the DataPath directory. This ensures that the data index remains up-to-date with the latest information.
	"""
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
