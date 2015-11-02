In the previous section we covered looping over lists using the `range()` and `len()` functions. Now you will learn about an easier way of directly looping over a list.

## for ... in list

{Run code}(python3 run-user.py content/1-lists/for_in_list.py)

We can use the same method for looping over a range of indexes to directly loop over a list for example:

```python
myList = [1,3,5,7,9]

for element in myList:
  print(element)
```

## When to use range()

So why would you use the first method? Well sometimes you want to control the `step` or change the values in the original list and to do that you need to loop using indexes and therefore the `range()` function.
