#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'split.py'
run_python_test '1,2,3,4,5,6,7,8,9' $'[1, 3, 5, 7, 9]\n[2, 4, 6, 8]'
run_python_test '1,3,5' $'[1, 3, 5]\n[]'
end_python_test
