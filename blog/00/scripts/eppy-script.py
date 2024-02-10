from eppy import modeleditor
from eppy.modeleditor import IDF
from eppy.easyopen import easyopen

idfpath = "1ZoneUncontrolled.idf"
idf = easyopen(idfpath)
building = idf.idfobjects['BUILDING'][0]
building.North_Axis = 45

idf.saveas("1ZoneUncontrolled_out.idf")
