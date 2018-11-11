#saveDAT Library for python3
#
#library for pausing and restoring python
#enviroments as well as saving individual
#variables of all types
#
#By: Ari Stehney

import json, sys, os, time, inspect

#Data Loader Caches
savedat = dict()
local_list = locals()
loadin = os.path.dirname(os.path.realpath(__file__)) + "/DatENV.txt"

# setup loader file and load it
def setloader():
    loadlink()

# load set data file
def loadlink():
    if os.path.exists(loadin) != True:
        with open(loadin, mode='w') as ta:
            ta.write("{}")
    with open(loadin, mode='r') as fa:
        if str(fa.read())=="":
            fa.close()
            with open(loadin, mode='w') as ta:
                ta.write("{}")
    with open(loadin, mode='r') as fa:
        link = json.load(fa)
        for item in link:
            savedat[item] = link[item]
    

# save variable dictionary
def savelink():
    with open(loadin, mode='w') as faa:
        faa.write(json.dumps(savedat))

# write var
def write(obj, data):
    savedat[obj]=data
    savelink()

# read var
def read(obj):
    return savedat[obj]

# output raw env dict
def raw():
    return savedat

# save current program enviroment to ouput file (DELETES ALL EXISTING DATA IN SAVEDAT)
def pause_env():
    savedat={}
    for item in local_list:
        #if (str(item)[0]!="_") and (item!="savedat") and (item!="olddat") and (item!="oldenv") and (item!="loadin"):
        if not((type(local_list[item])==type) or (inspect.isfunction(local_list[item])) or (inspect.isclass(local_list[item])) or (inspect.ismodule(local_list[item])) or (item=="savedat") or (item=="local_list") or (item=="loadin") or (str(item).startswith("__"))):
            write(item, local_list[item])
            print(item)
    savelink()
    
# restore enviroment vars
def restore_env():
    globals().update(savedat)

# restores old enviroment before the restore from file
def restore_old_env():
    for item in oldenv:
        eval(str(item)+" = "+oldenv[item])

# restores last state
def undo_modif():
    savedat = olddat
