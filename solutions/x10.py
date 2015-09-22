
input0 = input0([1, 2, 3, 4, 5, 6])
input1 = input1(5)
input2 = input2(3)

for i in range(input2 - 1, len(input0), input2):
  input0[i] = input0[i] * input1

output(input0)
