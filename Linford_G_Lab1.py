
######################################################
#  Linford_G_Lab1.py
#  Grant Linford
#  GEOG 181C
#  IDLE Version 3.9.6 
#  04/03/2022


#prints the string 'Hello World'
print('Hello World')

print('')#creates space between outputs

'''
This coding section allows users to input their own values for a given rectangle
After the user inputs their values the code returns the rectangle's area
This includes math and string handling
'''

#length and width are assigned user inputs that are classified as integers
length = int(input('Insert the length of a given rectangle: '))
width = int(input('Insert the width of a given rectangle: '))

#area is assigned the product of 'length' and 'width'
area = width * length

#prints a concatenated string with the integer 'area' as a string
print('The area of your rectangle is' +' '+str(area))

print('')#creates space between outputs

'''
This code is going to use a if, else statement in relation to the rectangle area calculator above
Depending on which statement the user input satisfies a corresponding message will be printed 
'''

#if else statement to test the variable 'area' related to the rectangle
if area > 10:
    print("That's a pretty big rectangle")
elif area <= 10:
    print("That's a small rectangle")
else:
    print("Do you not have a rectangle?")

print('')#to create space between outputs

'''
For loop section: this code uses a for loop to return values that exist within the studylist variable
'''

#studylist is an array given the following values related to my class schedule
studylist = ["GEOG 181C", "GEOG 182B", "GEOG 185"]
for item in studylist: #iterates each value in studylist
  print(item) #prints values in studylist

print('')#to create space between outputs


'''
while loop section: this code continuously increments a variable while a specified condition is proven true
when the specified condition is no longer true the code stops incrementing the variable
'''

#variable i is given value of 1
i = 1

#returns string for user context
print("Let's count to 10!")

#increments variable 'i' by a value of 1 until 'i' is equal to 10
#then prints a string to signal the end of the process
while i <= 10 :
  print(i) 
  if i == 10:
      print("We have arrived")
  i += 1 #increments 'i' by 1

print('')#to create space between outputs

'''
string indexing: the code below will assign a string to a variable
then use an index function to analyze the placement of a given character within the string
afterward 'pssplit' is created to turn the entire string into a list itself
'''

#variable 'ps' assigned a string
ps = "I am learning how to code"

x = ps.index("g") #this index calls the first instance of the letter 'g' in variable 'ps'

print(x)#this returns the first instance of 'g' in the string 'ps'

pssplit = ps.split()#'pssplit'takes variable 'ps' and turns it into a list
print(pssplit)#prints pssplit

print('')#to create space between outputs

'''
list indexing: these are geography courses that have been assigned to the variable 'geogcourses'
these courses can be called and printed using brackets and their associated number within the 'geogcourses' list
'''

#assigns various geography courses to variable 'geogcourses'
geogcourses = ['GEOG 181C', 'GEOG 182B','GEOG 185', 'GEOG 181A', 'GEOG 7']
print('these are some geography courses I have taken: ')
print('Geography class 1 = '+geogcourses[0])#this prints the first value in the list, and so on
print('Geography class 2 = '+geogcourses[1])
print('Geography class 3 = '+geogcourses[2])
print('Geography class 4 = '+geogcourses[3])
print('Geography class 5 = '+geogcourses[4])
print('All of the geography courses = '+str(geogcourses[0:4]))#this prints all of the values in 'geogcourses' at once as they are listed
print('Geography course list backwards = '+str(geogcourses[::-1]))#this prints 'geogcourses' from right to left

print('')#to create space between outputs

'''
File handling: this code will write to 'demos.txt' and print a confirmation in the python shell
'''

#variable 'f' is assigned open function on a file 
f = open('/Users/grantlinford/Desktop/Programming in arc/demos.txt', 'a')
f.write("This is new text being appended\n")#a string is appended to the existing text file
print("File has been written to.")

#opens 'f' and reads the appended sentences
f = open('/Users/grantlinford/Desktop/Programming in arc/demos.txt', 'r')
print(f.read())
f.close()#closes 'f' after reading text

del(f)#deletes 'f'






