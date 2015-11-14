
# Get our numbers from the command line
import sys
numbers= sys.argv[1].split(',')
numbers= [int(i) for i in numbers]

# Your code goes here
max = 0
pos = -1

for i in range(0, len(numbers)):
  if numbers[i] > max:
    max = numbers[i]
    pos = i

print(pos)