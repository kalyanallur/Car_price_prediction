import os
import pickle

def savefile(filepath, obj):
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)