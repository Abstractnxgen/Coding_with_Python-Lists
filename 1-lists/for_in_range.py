
myList = [1,3,5,7,9]

stop = len(myList)
print('the list has ' + str(stop) + ' elements')

aRange = range(0, stop)

for i in aRange:
  print(myList[i])

  
# short version  

print('a shorter way of creating ranges for looping')

for i in range(0, len(myList)):
  print(myList[i])
  

# display every second item

print('range step of 2')

for i in range(0, len(myList), 2):
  print(myList[i])
