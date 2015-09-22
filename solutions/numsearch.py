
input0 = input0([1,3,11,42,12])
input1 = input1(42)

found = 0

for i in range(0, len(input0)): 
  if input0[i] == input1:
    found = i
    # The break statement exits the loop
    break

if found == 0:
  output(-1)
else:
  output(found)
  