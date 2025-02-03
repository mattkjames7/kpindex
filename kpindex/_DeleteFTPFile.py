import os

def _DeleteFTPFile(fname):
	"""
	
	Removes a specified file from the filesystem using the `os.remove` method.
	
	This function calls the system's file removal capabilities to delete a file after data conversion is complete.
	
	Args:
	    fname (str): The full path to the file that needs to be deleted.
	
	Returns:
	    None: This function does not return a value.
	
	Raises:
	    FileNotFoundError: If the file specified by `fname` does not exist.
	    PermissionError: If the file exists but the operation lacks permission to delete it.
	
	"""
	os.remove(fname)
	
