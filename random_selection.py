import arcpy
import random

def generateStratifiedRandomSample(selectFromLayer, featureName, stratifyBy, fromStrata):

    layerDict = {}

    rows = arcpy.SearchCursor(selectFromLayer)

    for row in rows:
        
        feature = getattr(row, featureName)
        
        stratus = getattr(row, stratifyBy)
        
        if not stratus in layerDict: layerDict[stratus] = []
        
        layerDict[stratus].append(feature)
        
        del row
        
    del rows

    outDict = {}

    for stratus in layerDict.keys():

        if len(layerDict[stratus]) >= fromStrata:

            outDict[stratus] = []

            while len(outDict[stratus]) < fromStrata:

                randomIndex = int(random.uniform(0, len(layerDict[stratus])))

                randomEntry = layerDict[stratus][randomIndex]

                if not randomEntry in outDict[stratus]:

                    outDict[stratus].append(randomEntry)

    return outDict

def main(selectFromLayer, featureName, stratifyBy, fromStrata):

    samples = generateStratifiedRandomSample(selectFromLayer, featureName, stratifyBy, fromStrata)

    for state in samples:

        print state

        for sample in samples[state]:

            print "\t" + sample

    
if __name__ == "__main__":

    selectFromLayer = u'P:\GIS_Data\Hook\OhioRiver\CompletelyWithinRegion5.shp'

    featureName = 'NAME'

    stratifyBy = 'STATE_NAME'

    fromStrata = 5

    main(selectFromLayer, featureName, stratifyBy, fromStrata)
