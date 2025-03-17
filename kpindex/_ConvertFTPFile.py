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
	'''
	Converts standard KP ASCII files to binary.
	
	Inputs:
		FullPath: full apth and file name of the input file
		fname: just the name of the input file
		UpdateDate: The date which this was last upated on the OMNI site.
	
	'''
	#read the file
	out = _ReadKpTxt(FullPath)
	
	#get the date yyyymm	
	Year = out.Date[0]//10000
	
	#save file
	outfname = f"Kp-{Year:04d}.bin"
	outpath = f"{Globals.DataPath}/bin"
	if not os.path.isdir(outpath):
		os.makedirs(outpath)
	RT.SaveRecarray(out,f"{outpath}/{outfname}")
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
