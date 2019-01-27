#saveDAT Library for python3
#
#library for pausing and restoring python
#enviroments as well as saving individual
#variables of all types
#
#By: Ari Stehney
#
# The is encapsulated my MIT License

import json, sys, os, time, inspect, librarywrapper, clouddat, state

librarywrapper.CUSTOM_LOADER()
#Data Loader Caches
cloudmode=False
savedat = dict()
local_list = locals()
if not librarywrapper.LOADIN_CUSTOM:
    loadin = os.path.dirname(os.path.realpath(__file__)) + "/DatENV.txt"
else:
    loadin = librarywrapper.CUSTOM_LOADIN_CONTENTS
# setup loader file and load it
def setloader(ip="", user="", passwd="", clm=False,timeout=15, port=139, name_port=137, direct_tcp=False):
    loadlink(ip, user, passwd, clm, timeout, port, name_port, direct_tcp)

# load set data file
def loadlink(ip, user, passwd, clmode=False, timeout=15, port=139, name_port=137, direct_tcp=False):
    cloudmode=clmode
    if not cloudmode:
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
    else:
        clouddat.mountcloud(ip, user, passwd, timeout, port, name_port, direct_tcp)
        with clouddat.smb_fs.open(loadin, mode='r') as fa:
            if str(fa.read())=="":
                fa.close()
                with clouddat.smb_fs.open(loadin, mode='w') as ta:
                    ta.write("{}")
        with clouddat.smb_fs.open(loadin, mode='r') as fa:
            link = json.load(fa)
            for item in link:
                savedat[item] = link[item]
    state.LoadEntryPoint(savedat)
    del state.logState["logdat"]
    

# save variable dictionary
def savelink(sharename="Network"):
    if not librarywrapper.CUSTOM_SAVE:
        if not cloudmode:
            with open(loadin, mode='w') as faa:
                faa.write(json.dumps(savedat))
        else:
            savedat.savecloud(sharename, json.dumps(savedat))
    else:
        librarywrapper.CUSTOM_SAVE_FUNCTION()

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
    savedat["logdat"] = state.logState
    savelink()
    
# restore enviroment vars
def restore_env():
    globals().update(savedat)
    state.EntryPointRun()

# restores old enviroment before the restore from file
def restore_old_env():
    for item in oldenv:
        eval(str(item)+" = "+oldenv[item])

# restores last state
def undo_modif():
    savedat = olddat
