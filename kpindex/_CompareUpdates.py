from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	Compare the FTP data with local data to determine which files need updating.
	
	    Args:
	        newdates (list): A list of update dates as read from the FTP site.
	        newfiles (list): A list of original file names from the FTP site.
	        idx: An object containing the local index of stored data files, including attributes 'OldFileName' and 'UpdateDate'.
	
	    Returns:
	        numpy.ndarray: A Boolean array indicating which files need to be updated, where True signifies that the file requires an update.
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
		
