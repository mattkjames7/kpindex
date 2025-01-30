from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	"""
	Compare Updates Routine
	All text here is placeholder for the actual docstring.
	This includes the function's purpose, inputs, outputs,
	and any other relevant information.
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
		
