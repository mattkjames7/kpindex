from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
    """
    Determines which files from an FTP site require updating based on file names and modification dates.  
    
    Args:
        newdates (list): A list of modification dates for the files as read from the FTP site.
        newfiles (list): A list of original file names from the FTP site.
        idx (object): An object containing information about locally stored data files, including a list of old file names and update dates. 
    
    Returns:
        array(bool): A Boolean array indicating whether each file from the FTP site requires updating.
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
