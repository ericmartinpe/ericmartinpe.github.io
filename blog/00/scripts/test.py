# sample script - autosize all autosizable fields
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
from eppy import modeleditor
from eppy.modeleditor import IDF
from eppy import bunch_subclass
import os

iddfile = "C:/EnergyPlusV22-1-0/Energy+.idd"
IDF.setiddname(iddfile)

dir = os.path.dirname(os.path.realpath(__file__))
idf_dir = os.path.join(dir,'idfs')

for path, subdirs, files in os.walk(dir):
    for name in files:
        # print(os.path.join(path, name))
        ext = os.path.splitext(name)[-1].lower()
        if ext == ".idf":
            print(name)
            # idfpath = os.path.join(path, name)
            # idf = IDF(idfpath)
            # idfsave = os.path.join(path, "OffMed_eppy.idf")
            # idf.saveas(idfsave)
