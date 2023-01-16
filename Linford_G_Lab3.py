#Grant Linford
#GEOG 181C
#Lab 3
#04/16/2022


import arcpy #imports arcpy library
import math #imports math library

arcpy.env.overwriteOutput = True #allows tool to overwrite 

#sets parameters for user input or to be stored in tool's memory to be called again
buffIn = arcpy.GetParameterAsText(0) 
buffOut = 'memory/buffOut'
bufferDist = arcpy.GetParameterAsText(1)
intersectsWith = arcpy.GetParameterAsText(2)
intFeatures = [buffOut,intersectsWith]
outIntersect = 'memory/outIntersect'
countryIn = arcpy.GetParameterAsText(3)
spatial_join = 'memory/spatial_join'
tableOut = arcpy.GetParameterAsText(4)

#buffer analysis on user input and dissolves to avoid overlap
arcpy.analysis.Buffer(buffIn, buffOut, bufferDist, '', '', 'ALL', '', '')

#intersects user input of 'NA_Cities' to buffer
arcpy.analysis.Intersect(intFeatures, outIntersect, 'ALL', '', 'POINT')

#Joins attribute tables between memory -'outIntersect' and user input- 'North_America'
arcpy.analysis.SpatialJoin(outIntersect, countryIn, spatial_join)

#statistics analysis to find sum of attribute table variable Population
arcpy.analysis.Statistics(spatial_join, tableOut, [['Population', 'SUM'], ['POP_CNTRY','FIRST']], 'CNTRY_NAME')

#calculates a new field in 'tableOut' based on percentage of city's population compared to its country
arcpy.management.CalculateField(tableOut, 'Percent_Pop', '!SUM_population! / !FIRST_POP_CNTRY! *100')
