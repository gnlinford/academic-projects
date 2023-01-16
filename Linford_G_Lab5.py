#Grant Linford
#GEOG 181C
#05/01/2022


#imports relevant libraries
import os
import arcpy
import math

#defines folder paths for inputs and outputs
folder_path = r""
input_folder = os.path.join(folder_path, 'LabData')
output_folder = os.path.join(folder_path, 'output')
cntrd_file = os.path.join(output_folder, "NA_Big_Lakes_cntrd.shp")
bnd_file = os.path.join(output_folder, "NA_Big_Lakes_bnd.shp")

#sets up workspace in Arc
arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True

#defines a function to calculate distance
def distance_equation (x1, y1, x2, y2):
    equation = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2))
    return equation


#Part 1: City and Lake For-Loops
lakeFeature = "NA_Big_Lakes"
cityFeature = "NA_Cities"
lakeCopy = arcpy.management.Copy(lakeFeature, cntrd_file) #new file gets created in "output" folder through os.path.join

#adds relevant fields for minimum distance city and the actual distance
arcpy.management.AddField(lakeCopy, "min_city", "TEXT") 
arcpy.management.AddField(lakeCopy, "cntrd_dist", "DOUBLE") 

#creates empty list to populate with city centroid values
cityList = [] 

'''
First for loop to visit all cities and return their centroid coordinates using the token 'SHAPE@XY' and their names with
'CITY_NAME' in the search cursor, with-as statement then uses append module to populate 'cityList'
'''
with arcpy.da.SearchCursor(cityFeature, ["OID@", "CITY_NAME", "SHAPE@XY"]) as cityRows:
    for cntrd1 in cityRows:
        City = cntrd1[1]
        x, y = cntrd1[2] 
         
        cityList.append([x, y, City])
'''
Second nested for-loop structure to visit all lakes and then calculate euclidean distance between all point and polygon centroids
using UpdateCursor, previously created fields, and defined distance function
'''

cntrdDist = []
with arcpy.da.UpdateCursor(lakeCopy, ["OID@", "SHAPE@XY", "min_city", "cntrd_dist"]) as lakeRows: 
    for cntrd2 in lakeRows:
        x, y = cntrd2[1] #calls SHAPE@XY for polygon centroids
        for pnt in cityList:
            cntrdDist.append([distance_equation(x, y, pnt[0], pnt[1]), pnt[2], cntrd2[0]])#appends the distance and lake OID to cityList
        print(min(cntrdDist))# prints a list of the closest cities to lake
        cntrd2 [2] = min(cntrdDist)[1] #"min_city" field filled with the name of the closest city
        cntrd2 [3] = min(cntrdDist) [0] #"cntrd_dist" field filled with the distance of closest city

        cntrdDist = [] #resets list 'cntrdDist'
        lakeRows.updateRow(cntrd2) #update module for fields in list


print("Fields appended")


#Part 2: Boundary
lakeCopy2 = arcpy.management.Copy(lakeFeature, bnd_file) #2nd copy of lake shapefile

arcpy.management.AddField(lakeCopy2, "min_city", "TEXT") 
arcpy.management.AddField(lakeCopy2, "cntrd_dist", "DOUBLE") 

cntrdDist2 = [] 
with arcpy.da.UpdateCursor(lakeCopy2, ["OID@", "SHAPE@", "min_city", "cntrd_dist"]) as lakeRows2:
    for poly in lakeRows2: #iterates through lakes
        for line in poly[1]: #iterates through the lines in the polygons
            for vrtx in line: #iterates through each vertex comprising the lines
                if vrtx: 
                    for cntrd in cityList: #calculates the distance of between the points and cities
                        cntrdDist2.append([distance_equation(vrtx.X, vrtx.Y, cntrd[0], cntrd[1]), cntrd[2], poly[0]])
        print(min(cntrdDist2)) # prints a list of the closest cities to lake boundary
        poly [2] = min(cntrdDist2)[1] #field 'min_city' is filled with names of cities
        poly [3] = min(cntrdDist2) [0] #field 'cntrd_dist' is filled with closest distances

        cntrdDist2 = []
        lakeRows2.updateRow(poly)
