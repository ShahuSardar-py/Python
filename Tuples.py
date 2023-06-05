#-------------------------------------------------------------------------------
# Name:        Tuples
# Purpose:
#
# Author:      shahu
#
# Created:     05-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

tup = (1, 83, 29, 23, 65 , 23, 54)
print(tup)

#converting tuple to list and back to tuple

temp_list= list(tup)
temp_list.append(88)
temp_list.pop(0)

tup = tuple(temp_list)
print(tup)
