# State Sync API and Decorator Interface
# By: Ari Stehney
#
# State Sync for SaveDAT
# This program is encapsulated by the MIT License
#

import savedat, sys, clouddat, os

logState = dict()

class entrypoint(object):

    def __init__(self, arg1=""):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.arg1 = arg1
    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        def wrapped_f(*args):
            entrypoint = logState["entrypoint"]
            entrypoint["function"] = str(object.__name__)+"("
            entrypoint["arguments"] = eval("["+self.arg1.split(",")+"]")
            #f(*args)
        return wrapped_f

def LoadEntryPoint(inputdat):
    if "logdat" in inputdat:
        logState=inputdat["logdat"]

def EntryPointRun():
    if "entrypoint" in logState:
        exec(logState["entrypoint"]["function"]+logState["entrypoint"]["arguments"]+")")