
# Get our input from the command line
import sys
numbers = sys.argv[1].split(',')
for i in range(0,len(numbers)):
  numbers[i]= int(numbers[i])

def isEven(n) :
  return ((n % 2) == 0)

# Your code goes here
