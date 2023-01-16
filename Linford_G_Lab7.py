#Grant Linford
#GEOG181C
#05/15/2022


#imports necessary libraries
import arcpy, os, arcpy.mp, math

#sets up folder pathways
folder_path = r'C:\Users\GL558212\Desktop\Week 7 Programming'
input_folder = os.path.join(folder_path, 'LabData')
output_folder = os.path.join(folder_path, 'output')
ctyshp = os.path.join(input_folder, 'NA_Cities.shp')
lakeshp = os.path.join(input_folder, 'NA_Big_Lakes.shp')
nashp = os.path.join(input_folder, 'North_America.shp')

#sets up work environment
arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True

#variable created for final mapbook
finalPDF_fname = output_folder+'/Linford_G_Lab7.pdf'

#if the mapbook already exists it is removed
if os.path.exists(finalPDF_fname):
    os.remove(finalPDF_fname)

#creates the final product as a PDF object
finalPDF = arcpy.mp.PDFDocumentCreate(finalPDF_fname)

#sets up temporary pdf space to append layouts to final product
tmpPDF = input_folder+'/tmp.pdf'

#defines the arc project pathway
aprx = arcpy.mp.ArcGISProject(folder_path+'/Linford_G_Lab7.aprx')

#lists project layouts
Layout = aprx.listLayouts()[0]

#declares the mapframe as an element for manipulation
theMapFrame = Layout.listElements('MAPFRAME_ELEMENT')[0]

#sets cover page extent to cover majority of North American Lakes
overview_ext = arcpy.Extent(-2187141.0, -1226333.0, 2821041.0 , 4658607.0)
theMapFrame.camera.setExtent(overview_ext)
theMapFrame.camera.scale = theMapFrame.camera.scale *1.2

#if there is an existing version of the mapbook in os pathway it is removed
#cover page is exported to 'tmpPDF'
if os.path.exists(tmpPDF):
    os.remove(tmpPDF)
Layout.exportToPDF(tmpPDF)

#appends cover page pdf to final product
finalPDF.appendPages(tmpPDF)

#defines elements to be referenced in for loop
elm1 = Layout.listElements()[0]

#for loop statement that updates extent, area, and FID based on current layout
#deletes existing tmpPDF to export next iteration of layout
#appends tmpPDFs of 18 layouts to final mapbook product
with arcpy.da.SearchCursor(lakeshp, ['SHAPE@', 'FID', 'Area_km2'])as updateLay:
    for rows in updateLay:
        ext = rows[0].extent
        theMapFrame.camera.setExtent(ext)
        theMapFrame.camera.scale = theMapFrame.camera.scale *1.2
        elm1.text = 'FID: '+str(rows[1]) +' Lake Area: '+str(rows[2])
        if os.path.exists(tmpPDF):
            os.remove(tmpPDF)
        Layout.exportToPDF(tmpPDF)
        finalPDF.appendPages(tmpPDF)

#saves and closes the mapbook for next use
finalPDF.saveAndClose()

#cleans up variables 
del aprx, finalPDF, theMapFrame, elm1 #layout_el, elm1, #elem 


print('Mapbook Created')




