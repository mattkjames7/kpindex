import os
from . import Globals
import numpy as np
import PyFileIO as pf
import RecarrayTools as RT
import DateTimeTools as TT
from ._ReadDataIndex import _ReadDataIndex
from ._UpdateDataIndex import _UpdateDataIndex
from ._ReadKpTxt import _ReadKpTxt

def _ConvertFTPFile(FullPath,fname,UpdateDate):
	"""
	Converts standard KP ASCII files to binary format for storage in the data archive.
	
	Inputs:
		FullPath: Full path and filename of the input file
		fname: Just the name of the input file
		UpdateDate: The date this file was last updated on the OMNI site
	
	Output:
		Saves the converted file as a binary file with a naming scheme that includes the year (e.g., Kp-YYYYMM.bin) in the data directory. It also updates an index file to reflect the new file entry and its update date.
	"""
	#read the file
	out = _ReadKpTxt(FullPath)
	
	#get the date yyyymm	
	Year = out.Date[0]//10000
	
	#save file
	outfname = 'Kp-{:04d}.bin'.format(Year)
	outpath = Globals.DataPath+'bin/'
	if not os.path.isdir(outpath):
		os.makedirs(os.path.dirname(outpath))
	RT.SaveRecarray(out,outpath+outfname)
	print('Saved file: '+outfname)
	
	#update index
	idx = _ReadDataIndex()
	use = np.where(idx.OldFileName == fname)[0]
	if use.size == 0:
		#this file does not yet exist within the index file
		tmp = np.recarray(1,dtype=idx.dtype)
		tmp[0].FileName = outfname
		tmp[0].OldFileName = fname
		tmp[0].UpdateDate = UpdateDate
		idx = RT.JoinRecarray(idx,tmp)
	else:
		#file exists, update the information
		idx[use[0]].FileName = outfname
		idx[use[0]].OldFileName = fname
		idx[use[0]].UpdateDate = UpdateDate
	_UpdateDataIndex(idx)
