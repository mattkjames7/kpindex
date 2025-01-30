import os

def _DeleteFTPFile(fname):
	"""
	This function deletes a file on the local filesystem using the `os.remove()` method.
	
	The function takes one required argument, `fname`, which is the full path to the file you want to remove. This allows for flexible file location handling.
	
	The function does not perform any error checking beyond what is provided by the underlying `os.remove()` method. It assumes that the caller ensures that `fname` is a valid and existing file.
	
	This implementation leverages Python's built-in `os` module to handle file removal, ensuring portability across different Unix-based systems.
	"""
	os.remove(fname)
	
