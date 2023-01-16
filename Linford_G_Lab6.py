#Grant Linford
#GEOG 181C
#05/08/2022

#imports relevant libraries and Spatial Analyst Toolbox
import arcpy
import os
import arcpy.sa
import math

#sets up folder pathways 
folder_path = r'C:/Users/GL558212/Desktop/Week 6 Programming'
input_folder = os.path.join(folder_path, 'LabData')
output_folder = os.path.join(folder_path, 'output')
transfer_ndvi = os.path.join(output_folder, 'Lab_NDVI.tif')
transfer_remap = os.path.join(output_folder, 'Lab_NDVI_Remap.tif')
rasterData = os.path.join(input_folder,'Landsat.TIF')

#sets arcpy workspace
arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True


#Step 1: Printing out image properties

desc = arcpy.Describe(rasterData) #sets 'desc' as variable to call rasterData information
print(rasterData + ' Spatial Projection: ' +desc.spatialReference.Name + ' # of Bands' +str(desc.bandCount))#returns called raster image information 

bandCount = desc.bandCount #sets variable bandCount to desc.bandCount 6
for MyNumber in range(1, 2):#evaluating values for 1 band because range is 1,2
    MyBand = '/Band_' +str(MyNumber)#for each band from 1 to however many 
    desc = arcpy.Describe(rasterData + MyBand)#describe MyBand in relation to original 'RasterData'
    #prints out the following values of the raster image's bands
    print('# of X pixels: '+ str(desc.width),'# of Y pixels: ' + str(desc.height), 'Image Resolution: ' +str(desc.meanCellHeight), desc.spatialReference.linearUnitName)


del desc
print('Raster Image Specs Listed')


#Step 2: Create a function to compute NDVI using appropriate bands

ndviDem = arcpy.Raster(rasterData)
NIR = arcpy.Raster(rasterData+'/Band_4')#sets NIR band as raster object
Red = arcpy.Raster(rasterData+'/Band_3')#sets red band as raster object

NDVI = ((NIR - Red) / (NIR + Red))#calculates for NDVI values using NIR and Red bands
NDVI.save('NDVI_result.tif')#saves result of NDVI calculation
ndviOut = arcpy.management.Copy('NDVI_result.tif', transfer_ndvi)#creates a copy of the ndvi to output

print('NDVI Function Computed')


#Step 3: Generate a separate NDVI category raster using the following ranges


NDVI_copy = arcpy.Raster('NDVI_result.tif')#declares NDVI_result.tif as a raster object for manipulation



ndvi_remap = arcpy.sa.RemapRange([[-1,0,1], [0.0, 0.3, 2], [0.3, 1, 3]])#sets the parameters for reclassifying the ndvi

outRemap = arcpy.sa.Reclassify(NDVI_copy, 'VALUE', ndvi_remap)#reclassifies values based on remap criteria
outRemap.save('NDVI_Remapped.tif')#saves remapped NDVI

print('NDVI Reclassified')


##Step 4: Output the NDVI value and associated categorical value at location

remappedRas = arcpy.Raster('NDVI_Remapped.tif') #Declares 'NDVI_Remapped.tif' as raster object
remapOut = arcpy.management.Copy('NDVI_Remapped.tif', transfer_remap) #Creates a copy of the remapped ndvi to output
ndvi_value = arcpy.management.GetCellValue(NDVI_copy, '349908 3768856', '')#retrieves cell values of ndvi raster at listed coordinates for all bands 3/4
reclass_value = arcpy.management.GetCellValue(remappedRas, '349908 3768856', '')#retrieves cell values of remapped ndvi at listed coordinates for bands 3 and 4
print('NDVI value at 349908, 3768856: '+str(ndvi_value))#prints cell values for ndvi
print('Remapped NDVI Value at 349908, 3768856: '+str(reclass_value))#prints cell values for remapped ndvi

print('Cell Values Retrieved')


