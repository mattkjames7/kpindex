import os

def _DeleteFTPFile(fname):
	"""
	Delete FTP file using the 'rm' command.
	
	Args:
	    fname (str): Full path to file to remove.
	"""
	os.remove(fname)
	
