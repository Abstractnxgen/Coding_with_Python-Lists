There are two main ways for looping over lists. The first way covered in this section uses the `len()` and `range()` functions to create a list of indexes to loop over. The indexes are then used to get the content from your original list.

## for .. in range

{Run code}(python3 run-user.py content/1-lists/for_in_range.py)

The `len()` function returns the length of the list supplied as an argument.

With the length we now know up to where we must iterate. Using the `range(start, stop)` function we can create a range between the value of `start` and `stop` for example:

```python
myList = [1,3,5,7,9]

stop = len(myList)
print('the list has ' + str(stop) + ' elements')

# we are supplying a start value of 0
aRange = range(0, stop)
```

`aRange` will have a value of `[0,1,2,3,4]`.

The for loop will then step over each element in the range. 

```python
for i in aRange:
  print(myList[i])
```

Each `i` will be used as an index to reference the items in `myList` for example:

```python
i = 0
# value of 1
myList[i]

i = 1
# value of 3
myList[i]
```

We can also combine all the steps in to one line to make it easier to read.

```python
myList = [1,3,5,7,9]

# one line to check the length of the list 
# and create a range to loop over 
for i in range(0, len(myList)):
  print(myList[i])
```

## range() step

You can supply a third argument to range, the range `step`, which tells Python what value to step between `start` and `stop`. If no `step` is given a value of `1` is used.

```python
myList = [1,3,5,7,9]

## will display every second item
for i in range(0, len(myList), 2):
  print(myList[i])
```
