{Check It!|assessment}(test-1116072670)

|||guidance
### Solution
```python
# Get our numbers from the command line
numbers= sys.argv[2]

# Your code goes here
max = 0
pos = -1

for i in range(0, len(numbers)):
  if numbers[i] > max:
    max = numbers[i]
    pos = i

print(pos)
```
|||
