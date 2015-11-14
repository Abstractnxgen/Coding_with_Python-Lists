{Check It!|assessment}(test-3916901719)

|||guidance
### Solution
```python
# Get our list from the command line
import sys
numbers = sys.argv[1].split(",")

# Your code goes here
total = 0

for i in numbers:
  total = total + int(i)

print(total)
```
|||
