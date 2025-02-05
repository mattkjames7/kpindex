from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	
	Compare the update dates and file names from an FTP site with local data to
	identify which files need to be updated.
	
	Args:
	    newdates (list): List of update dates retrieved from the FTP site.
	    newfiles (list): List of original file names from the FTP site.
	    idx (object): Local index of stored data files, expected to contain
	attributes OldFileName and UpdateDate.
	
	Returns:
	    np.ndarray: A boolean array where True indicates that a file needs to be
	updated, and False indicates that it does not.
	
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
		
