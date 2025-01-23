from . import Globals
import PyFileIO as pf
import numpy as np
import datetime

months = { 	'Jan':1,
			'Feb':2,
			'Mar':3,
			'Apr':4,
			'May':5,
			'Jun':6,
			'Jul':7,
			'Aug':8,
			'Sep':9,
			'Oct':10,
			'Nov':11,
			'Dec':12 }

def _ListFiles(currYear):

    """
    Generates a list of file names based on the provided year. 
    
    The function creates a list of strings representing Kp_ap files for each year from 1932 up to and including the given `currYear`. Each file name follows the pattern 'Kp_ap_{:04d}.txt', where {:04d} is replaced with the corresponding year.
    
    Args:
        currYear (int): The current year for which file names are to be generated.
    
    Returns:
        list: A list of strings representing the file names in the desired format.
    """
	#we need a list of specific file names
	#as this directory oin the FTP site now
	#stores multiple different types of files
	years = np.arange(1932,currYear+1)
	fnames = ['Kp_ap_{:04d}.txt'.format(y) for y in years]

	return fnames
def _ParseFTP():
    """
      
    Reads the FTP index file and extracts file names, associated update dates, and FTP addresses.
    
       The function retrieves a list of files from a predefined source (based on the current year) and then parses an HTML file named 'index.html' located in the 'tmp' directory under the 'DataPath' specified in Globals.  It identifies lines containing specific file names ('omni_min' or 'omni_5min'), extracts relevant data such as the update year, month, day, FTP address, and file name.
    
       Args:
            None
    
        Returns:
          tuple: A tuple containing three arrays:
             - FileNames (ndarray): An array of extracted file names.
             - Addresses (ndarray): An array of corresponding FTP addresses.
             - UpdateDates (ndarray): An array of update dates in the format 'YYYYMMDD'.
       
    """
	

	#get the current year
	today = datetime.datetime.today()
	currYear = np.int32(today.strftime('%Y'))

	#list of files to look for
	files = _ListFiles(currYear)

	#read the file in
	fname = Globals.DataPath+'tmp/index.html'
	lines = pf.ReadASCIIFile(fname)
	nl = np.size(lines)
	
	#firstly, search for the lines which contain 'omni_min' or 'omni_5min'
	use = np.zeros(nl,dtype='bool')
	for i in range(0,nl):
		isgd = False
		for f in files:
			if f in lines[i]:
				isgd = True
		if isgd:
			use[i] = True
	keep = np.where(use)[0]
	lines = lines[keep]
	nl = lines.size
	
	#now to extract the FTP address, file name and update dates
	UpdateDates = np.zeros(nl,dtype='object')
	Addresses = np.zeros(nl,dtype='object')
	FileNames = np.zeros(nl,dtype='object')
	
	# note: negative indices are important because additional data in some lines
	for i in range(0,nl):
		#deal with date first
		s = lines[i].split()	
		if ':' in s[-2]:
			yr = currYear
		else:
			yr = np.int32(s[-2])
		mn = months[s[-4]]
		dy = np.int32(s[-3])
		UpdateDates[i] = '{:08}'.format(yr*10000 + mn*100 + dy)
		
		#now let's get the ftp address
		Addresses[i] = Globals.ftpadress + s[-1]
		
		#now the file name
		FileNames[i] = s[-1]
		
	return FileNames,Addresses,UpdateDates