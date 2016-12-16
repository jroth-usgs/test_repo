# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 14:02:47 2016

@author: jroth

desc - goes through a directory and converts array files to ascii files.

input -

in_dir = str - input directory containing array files

fext =  str - file extension to convert into asciis

tpl_grd = str - path to grid that has same bounds as arrays

grd_typ = lst - list of strings with array property names

output -

out_dir = str - path to output directory, will create it if dne

"""
### import modules ############################################################
import ascii as asc
import os
import numpy as np
### user defined variables ####################################################

in_dir = "D:\\GWmodels\\current\\for_pres\\model\\arrays"

fext =  "arr"

grd_typ = []

tpl_grd = 'D:\\GWmodels\\current\\pest_testing\\model\\tables\\brk_dom_grd.asc'

out_dir = "D:\\GWmodels\\current\\for_pres\\model\\arrays\\ascii"



### main code execution #######################################################

tpl = asc.asciiGrid(tpl_grd)
tpl.change_type('float')
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for f in os.listdir(in_dir):
    if f.split('.')[-1] == fext:
        if len(grd_typ) > 0:
            for t in grd_typ:
                if t in f:
                    tpl.data = np.genfromtxt(os.path.join(in_dir,f))
                    tpl.export_grid(os.path.join(out_dir,f.split('.')[0]+".asc"))
        else:
            tpl.data = np.genfromtxt(os.path.join(in_dir,f))
            tpl.export_grid(os.path.join(out_dir,f.split('.')[0]+".asc"),fmt='{0:1.4e}')