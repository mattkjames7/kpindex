import os

def _DeleteFTPFile(fname):
        """

        Remove the specified file from the filesystem.

        This function uses the `os.remove` method to delete a file at the given
path.

        Args:
            fname (str): The full path to the file that needs to be deleted.

        Raises:
            OSError: If the file does not exist or the function lacks the
permission to delete the file.


        """
	os.remove(fname)
	
