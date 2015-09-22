
input0 = input0([1, 2, 3, 4, 5, 6, 7, 8, 9])
oddList = []
evenList = []

for i in range(0, len(input0)):
  if input0[i] % 2 == 0:
    evenList.append(input0[i])    
  else:
    oddList.append(input0[i])

output(oddList)
output(evenList)
