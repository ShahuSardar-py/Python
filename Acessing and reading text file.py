#-------------------------------------------------------------------------------
# Name:        Acessing and reading text files.
# Purpose:
#
# Author:      Shahu
#
# Created:     19-05-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Simple way to read up text file

a= open('Shahu.txt', 'r')

firstline= a.readline()
secondline= a.readline()

print(firstline)
print(secondline)