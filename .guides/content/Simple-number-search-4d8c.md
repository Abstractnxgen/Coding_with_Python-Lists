{Check It!|assessment}(test-1147907621)

|||guidance
## Solution
```python
# Get our input from the command line
import sys
N= int(sys.argv[2])

# Convert the list of strings into integers
numbers= []
for i in sys.argv[1].split(","):
  if(i.isdigit()):
    numbers.append(int(i))

                   
# Write your code below

index= 0       # an index counter for the while loop
found= False   # a check to break out early once found

# loop until ew find the value or we are out of numbers
while (not found and index < len(numbers)):
  if numbers[index] == N:  # It this one it?
    found= True            # Yes - we are done
  else:
    index = index + 1      # No - move along to the next index
    
if not found:      # Did the loop find it?
  print(str(-1))   # No - answer is -1
else:              
  print(index)     # Yes - answer is the index we found

```
|||
