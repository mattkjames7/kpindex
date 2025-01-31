import os

def _DeleteFTPFile(fname):
	"""
	
	   Calls the linux rm command to remove the original data file after conversion.
	
	Args:
	    fname (str): Full path to file to delete.
	   '
	
	os.remove(fname)
	
	"""
	os.remove(fname)
	
