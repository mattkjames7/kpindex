import os

def _DeleteFTPFile(fname):
    """
    Removes a file from the local filesystem.
    
    Args:
        fname (str): The full path to the file to be deleted.
    """
	os.remove(fname)	
