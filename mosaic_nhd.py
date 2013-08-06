import os
import arcpy

homeDir = 'P:/GIS_Data/Hook/NHD_Medium'

index = {}
for folder in os.listdir(homeDir):
    fullpath = os.path.join(homeDir, folder)
    if os.path.isdir(fullpath):
        gdb = os.path.join(fullpath, "{0}.gdb".format(folder.split("_")[0]))
        if os.path.exists(gdb):
            arcpy.env.workspace = gdb
            if not index:
                for fds in arcpy.ListDatasets('','feature'):
                    index[fds] = []
                    for fc in arcpy.ListFeatureClasses('','',fds):
                        index[fds].append(fc)
    print index
    abra
