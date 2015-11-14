When working with an empty list, like `numList` in the code window on the left, we need a way of inserting new elemenets. 

{Run code}(python3 content/1-lists/append_insert.py)

## append()

A list's `append(element)` method will add an element to the end of the list.

```python
# append some items to the empty list
numList.append(1)
numList.append(2)
numList.append(4)

print(numList)
```

The code above will output 

```python
[1,2,4]
```

## insert()

If you want to add elemets at a specific location use a list's `insert(index, element)` method. The method inserts the element at the specific index in the list.

```python
numList.insert(2, 3)

print(numList)
```

The code above inserts `3` as the the third element, index `2`, in `numList`.


