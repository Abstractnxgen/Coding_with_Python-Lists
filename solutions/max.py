
input0 = input0([1, 5, 8, 23, 78, 22, 0])
max = 0
pos = -1

for i in range(0, len(input0)):
  if input0[i] > max:
    max = input0[i]
    pos = i

output(pos)
