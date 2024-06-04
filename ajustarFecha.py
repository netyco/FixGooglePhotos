import filedate, json, os 
import os
from os import listdir
from os.path import isfile, join
import datetime
from dateutil.parser import parse

import dateutil.parser as parser 

directorio = './'
contenido = (f.name for f in os.scandir() if not f.name.startswith('._'))







for filename in contenido:
    archivo = filename
    list=os.path.splitext(archivo)
    listCount=len(list)
    ext=list[listCount-1]

    if archivo!=".DS_Store":
        if ext!=".json":
            print(archivo)
            jsonFIle=archivo[0:46]+".json"

            if os.path.exists(jsonFIle):
                with open(jsonFIle, "r") as file:
                    data_object = json.load(file)

                ts= data_object['creationTime']['formatted']
                                
                ts= data_object['creationTime']['formatted']
                ts=ts.replace(" ene ","/01/")
                ts=ts.replace(" feb ","/02/")
                ts=ts.replace(" mar ","/03/")
                ts=ts.replace(" abr ","/04/")
                ts=ts.replace(" may ","/05/")
                ts=ts.replace(" jun ","/06/")
                ts=ts.replace(" jul ","/07/")
                ts=ts.replace(" ago ","/08/")
                ts=ts.replace(" sep ","/09/")
                ts=ts.replace(" oct ","/10/")
                ts=ts.replace(" nov ","/11/")
                ts=ts.replace(" dic ","/12/")

                try:
                    filedate.File(archivo).set(
                        created = ts,
                        modified=ts,
                        accessed=ts
                    )
                except Exception:
                    pass

