#Grant Linford
#GEOG 181C
#04/24/2022

#imports libraries
import arcpy
import os

#sets up workspace and defines folder paths
folder_path = r'C:/Users/GL558212/Desktop/'
input_folder = os.path.join(folder_path, 'LabData')
output_folder = os.path.join(folder_path, '')
arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True
fc = 'NA_Cities.shp'

#creates new table in 'output_folder' assigned to 'myTable'
myTable = arcpy.management.CreateTable(output_folder, 'City_Table') #creates dbf table 
#Method: Add fields into a new table
arcpy.management.AddField(myTable,'cityName', 'TEXT')
arcpy.management.AddField(myTable, 'countryName', 'TEXT')
arcpy.management.AddField(myTable, 'adminName', 'TEXT')
arcpy.management.AddField(myTable, 'population', 'DOUBLE')

#assigns 'addRow' to InsertCursor for dbf table
addRow = arcpy.da.InsertCursor(myTable, ['cityName','countryName','adminName','population'])

#SQL to find US cities that meet the specified criteria
USRows = []
US_delim = arcpy.AddFieldDelimiters(fc, 'Population')
SQL_US = US_delim + '>= 8000000'

#Searches 'NA_Cities.shp' for rows that match 'United States' and satisfy the previous SQL statement
with arcpy.da.SearchCursor(fc, ['CITY_NAME','CNTRY_NAME','ADMIN_NAME','Population'],SQL_US)as cursor:
    for row in cursor:
        if row[1] == 'United States':
            USRows.append(row)
#For loop to insert US values into 'myTable'
for USitem in USRows:
    addRow.insertRow(USitem)


#SQL Statement for Canada
CARows = []
CA_delim = arcpy.AddFieldDelimiters(fc, 'Population')
SQL_CA = CA_delim + '>= 3000000'

#Search cursor to find records in 'NA_Cities.shp' for Canada
with arcpy.da.SearchCursor(fc, ['CITY_NAME','CNTRY_NAME','ADMIN_NAME','Population'], SQL_CA)as cursor:
    for row in cursor:
        if row[1] == 'Canada':
         CARows.append(row)

#Inserts extracted rows into 'myTable'
for CAitem in CARows:
    addRow.insertRow(CAitem)

#SQL Statement for Mexico
MXRows = []
MX_delim = arcpy.AddFieldDelimiters(fc, 'Population')
SQL_MX = MX_delim + '>= 8000000'

#Search Cursor for Mexico
with arcpy.da.SearchCursor(fc, ['CITY_NAME','CNTRY_NAME','ADMIN_NAME','Population'], SQL_MX)as cursor:
    for row in cursor:
        if row[1] == 'Mexico':
            MXRows.append(row)

#For loops to iterate through extracted rows and insert into 'myTable'
for MXitem in MXRows:
    addRow.insertRow(MXitem)




'''
I was unsure of how to resolve this error
----------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/GL558212/Desktop/Linford_G_Lab4.py", line 40, in <module>
    addRow.insertRow(USitem)
SystemError: <method 'insertRow' of 'da.InsertCursor' objects> returned NULL without setting an error
>>> 
'''
