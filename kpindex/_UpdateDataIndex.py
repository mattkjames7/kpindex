import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
        """
        Updates the data index file with provided information.

        Args:
            idx (numpy.recarray): A structured array containing the file names,
time resolution, and dates for all data files.

        Returns:
            None: This function does not return a value.
        """
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)
