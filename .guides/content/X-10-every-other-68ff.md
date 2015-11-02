{Check It!|assessment}(test-4030970452)

|||guidance
### Solution
```python
# Get our input from the command line
numbers= sys.argv[2]
M= sys.argv[3]
N= sys.argv[4]

# Your code goes here
for i in range(N - 1, len(numbers), N):
  numbers[i] = numbers[i] * M

print(numbers)
```
|||
