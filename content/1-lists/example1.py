
# Get our lists from the command line
# It's okay if you don't understand this right now
import sys
list1 = sys.argv[1].split(',')
list2 = sys.argv[2].split(',')


#
# Print the lists.
# 
# Python puts '[]' around the list and seperates the items
# by commas.
print(list1)
print(list2)

#
# Note that this list has three different types of items
# in the container: an Integer, a String, and a Boolean.
# 
list3 = [1,"red", True]
print(list3)

