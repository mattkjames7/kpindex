from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	This routine compares the FTP data with local data to determine which files need updating. It checks each file from the FTP site against stored local files and their associated update dates. If a file exists locally but hasn't been updated, or if the date doesn't match, it marks that entry as needing an update.
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
		
