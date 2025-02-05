import os

def _DeleteFTPFile(fname):
	"""
	
	Deletes a specified file from the filesystem using the `os.remove` method.
	
	This function attempts to remove the file at the path specified by `fname`.
	If the file does not exist or another error occurs during deletion, an
	exception may be raised.
	
	Args:
	    fname (str): The full path to the file that is to be deleted.
	
	Raises:
	    FileNotFoundError: If the specified file does not exist.
	    PermissionError: If the user does not have permission to delete the file
	or if the file is read-only.
	    OSError: For other errors encountered during file removal.
	
	
	"""
	os.remove(fname)
	
