
import test

test.test('challenges/numsearch.py', [[1,3,11,42,12], 42], [3])
test.test('challenges/numsearch.py', [[1,3,11,42,12], 2], [-1])
test.test('challenges/numsearch.py', [[], 1], [-1])

print('Well done')