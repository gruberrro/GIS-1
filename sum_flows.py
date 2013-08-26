## Name: sum_flows.py
## Created by: James (Trip) Hook, US EPA/OPP/EFED/EISB
## Date created: 8/26/2013
## Descripton: Sum up flows in the feature class containing reach flow volumes,
## and join with existing NHD Plus v2 attributes and basin polygons
## Wishlist: 

from manipulate_fc import *

def clear_selection(layers):

    if not type(layers) == list: layers = [layers]

    for layer in layers:

        arcpy.SelectLayerByAttribute_management(layer, "CLEAR_SELECTION")

def get_wb_volume(drainage_basins, lines_with_flows, vol_field, basin_id):

    clear_selection([drainage_basins.lyr, lines_with_flows.lyr])

    arcpy.SelectLayerByAttribute_management(drainage_basins.lyr, "NEW_SELECTION", \
                                            "\"{0}\" = \'{1}\'".format(drainage_basins.id, basin_id))
    
    arcpy.SelectLayerByLocation_management(lines_with_flows.lyr, "INTERSECT", drainage_basins.lyr)

    output = sum(lines_with_flows.attribute_dict(vol_field).values())

    clear_selection([drainage_basins.lyr, lines_with_flows.lyr])

    return output
                          
def main(lines_with_flows, nhdplus_v2_lines, drainage_basins, vol_field, outfile):
    
    f = open(outfile, 'wb')

    f.write("Basin_ID,Volume\n")

    for basin_id in drainage_basins.attribute_dict().keys():

        print "Getting area for basin {0}...".format(basin_id)
    
        vol = get_wb_volume(drainage_basins, lines_with_flows, vol_field, basin_id)

        f.write("{0},{1}\n".format(basin_id, vol))

    f.close()

    print "Done. All volumes written to {0}".format(outfile)
        
if __name__ == '__main__':
    
    # Line shapefile containing flow volumes
    lines_with_flows = feature_class(r"P:\GIS_Data\NHD_Plus\Flowlines with flow attributes\NHDPlus5_flowinglines&attr.shp", "ReachCode")

    # NHD Plus v2 flowlines feature class
    nhdplus_v2_lines = feature_class(r"P:\GIS_Data\Hook\OhioRiver\SAM_HR5.gdb\NHDFlowline_Clip", "ReachCode")

    # Drainage basins polygon feature class
    drainage_basins = feature_class(r"P:\GIS_Data\SAM_HR05\Basins_FlowingWater\HR05_DWsheds_flowingwater.shp", "reachcode")

    vol_field = "Vol_m3"

    outfile = r"P:\GIS_Data\Hook\OhioRiver\basin_volumes.txt"
    
    main(lines_with_flows, nhdplus_v2_lines, drainage_basins, vol_field, outfile)
