import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
    """
    Updates the data index file.
    
    Args:
        idx (numpy.recarray): A NumPy recarray containing the file names, time resolution, and dates for all data files.
    
    Writes the updated data index to the 'DataIndex.dat' file located in the Globals.DataPath directory.
    """
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)