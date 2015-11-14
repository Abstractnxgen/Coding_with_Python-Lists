{Check It!|assessment}(test-4030970452)

|||guidance
### Solution
```python
# Get our input from the command line
import sys
M= int(sys.argv[2])
N= int(sys.argv[3])

numbers= sys.argv[1].split(',')
for i in range(0, len(numbers)):
  numbers[i]= int(numbers[i])

# Your code goes here
for i in range(N - 1, len(numbers), N):
  numbers[i] = numbers[i] * M

print(numbers)
```
|||
