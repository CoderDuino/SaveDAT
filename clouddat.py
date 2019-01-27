###########################################
# CloudDAT Extension for SaveDAT
# Written Be Ari Stehney
# Allows for Cloud Saving of Python ENV Status
#
# For SaveDAT by Ari Stehney
# The is encapsulated by the MIT License
###########################################
import librarywrapper, sys, os, sysconfig, inspect, fs.smbfs

import fs.smbfs
smb_fs = dict()

def mountcloud(ip, user, passwd, timeout=15, port=139, name_port=137, direct_tcp=False):
    smb_fs = fs.smbfs.SMBFS(
        ip, username=user, passwd=passwd, timeout=timeout,
        port=port, name_port=name_port, direct_tcp=direct_tcp
    )

def loadcloud(sharename):
    with smb_fs.open(sharename+"/Save.json",mode="r") as f:
        return f.read()
def savecloud(sharename, jsondump):
    with smb_fs.open(sharename+"/Save.json", mode="w") as f:
        f.write(jsondump)