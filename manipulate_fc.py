## Name: manipulate_fc.py
## Created by: James (Trip) Hook, US EPA/OPP/EFED/EISB
## Date created: 8/26/2013
## Descripton: Provides for easy manipulation of feature class
## Wishlist: 


import arcpy, random

# Creates an object to easily work with feature classes

class feature_class():

    def __init__(self, path, id_key):

        self.path = path # Create 'path' attribute containing full path to fc

        self.id = id_key # Field which contains 'key' identity used to join with other classes

        self.make_layer() # Creates a .lyr attribute to work with the fc as a layer


    def make_layer(self):

        while True:

            self.lyr = "lyr{0}".format(random.randint(0, 9999)) # Create a unique layer name using random number

            arcpy.MakeFeatureLayer_management(self.path, self.lyr)

            break

    # Read attributes for all features in fc and create a dictionary with id field contents as keys and specified field (val_key)
    # contents as values
    
    def attribute_dict(self, val_key = ''):

        out_dict = {}
        
        rows = arcpy.SearchCursor(self.lyr)

        for row in rows:

            part_id = getattr(row, self.id)

            if val_key:

                val = getattr(row, val_key)

            else:

                val = 'null'

            out_dict[part_id] = val

            del row

        del rows

        return out_dict



if __name__ == "__main__":

    # Import modules

    print "This is a class and function library only. Can be called with \"import manipulate_fc\""
