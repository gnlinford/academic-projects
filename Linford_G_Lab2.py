## Linford_G_Lab2.py
## Grant Linford
## GEOG 181C
## IDLE 3.9.6
## 04/10/2022

import os #imports os library to script

##Assignment Part 1 - Reading and Printing all files in LabData

folder_path = r'/Users/grantlinford/Desktop/Lab2 181C/LabData'#assigns 'folder_path' labdata pathway


os.chdir(folder_path)#change the directory to the folder_path. A directory is where your program is looking for input/output data
listFile = os.listdir(folder_path)
counting = 0 #variable assigned 0 to count along with printed output from for loop
for files in listFile: #prints objects in variable 'listFile'
    print(files)
    counting +=1


print('\n===========================')

##Assignment Part 2 - Reading and Printing Number of Shapefiles in LabData

fileCount = 0 #initializes 'fileCount'
for file in listFile: #for loop that prints objects in 'listFile' that end in '.shp' to return shapefiles
    if file.endswith('.shp'):
        print(str(file))
        fileCount += 1
        
print('There are',fileCount,' shapefiles in LabData')#prints string for contextualization for user

print('\n=============================')

##Assignment Part 3 - Buffer Geoprocessing in ArcGis Pro using Python

import arcpy #imports library 'arcpy' to script

environment_pathway = 'C:/Users/GL558212/Desktop/LabData' #'environment_pathway' is assigned a file pathway from remote desktop
buffer = '20 Kilometers'#assigns value of 20km to variable 'buffer'
arcpy.env.workspace = environment_pathway #declares 'environment_pathway' as working directory in ArcPro
arcpy.Buffer_analysis('NA_Cities.shp','City_buffer.shp',buffer)#applies a buffer analysis of 1km to the shapefiles within shapeList
    
