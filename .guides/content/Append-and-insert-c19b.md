`numList` in the code window on the left is an empty list. Below are some ways you could insert new elements to the list.

{Run code}(python3 content/1-lists/append_insert.py)

## append()

Using `append(element)` will add an element to the end of the list:

```python
# append some items to the empty list
numList.append(1)
numList.append(2)
numList.append(4)

print(numList)
```

The code above will output the following: 

```python
[1,2,4]
```

## insert()
Using `insert(index, element)` will add elements at a specific location. This method inserts the element into the list at the specific index given.

```python
numList.insert(2, 3)

print(numList)
```

The code above inserts `3` as the the third element, (which is at index `2`), in `numList`.


