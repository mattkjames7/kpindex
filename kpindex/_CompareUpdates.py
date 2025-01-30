from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	This routine compares the FTP data with local data to determine which files need updating.
	
	Args:
	    newdates (list): List of dates files were updated on the FTP site.
	    newfiles (list): List of file names from the FTP site.
	    idx (obj): Object containing local index data, including OldFileName and UpdateDate.
	
	Returns:
	    bool array indicating which files need to be updated.
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
		
