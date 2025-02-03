import os

def _DeleteFTPFile(fname):
	"""
	
	Remove a file from the filesystem.
	
	This function calls the Linux `rm` command to delete the specified file.
	
	Args:
	    fname (str): The full path to the file that needs to be deleted.
	
	Raises:
	    FileNotFoundError: If the specified file does not exist.
	    PermissionError: If the program does not have permission to delete the file.
	
	
	"""
	os.remove(fname)
	
