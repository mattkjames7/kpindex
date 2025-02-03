from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	
	Compare FTP data with local data to determine which files need updating.
	
	This function compares the update dates and filenames from an FTP source with
	the locally stored data, identifying which files should be refreshed based
	on discrepancies in update dates or if the files do not exist locally.
	
	Args:
	    newdates (list): A list of update dates retrieved from the FTP site.
	    newfiles (list): A list of original file names from the FTP site.
	    idx (object): An object containing the local index of stored data files,
	        which includes attributes `OldFileName` and `UpdateDate`.
	
	Returns:
	    numpy.ndarray: A boolean array indicating which files require updates.
	
	
	"""
	
	nf = np.size(newfiles)
	update = np.zeros(nf,dtype='bool')
	for i in range(0,nf):
		#check if new file matches old file
		if newfiles[i] in idx.OldFileName:
			use = np.where(idx.OldFileName == newfiles[i])[0][0]
			#compare update dates
			if newdates[i] != idx.UpdateDate[use]:
				update[i] = True
		else:
			#if we get to this point then we need to update
			update[i] = True
	
	return update
		
