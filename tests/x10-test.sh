#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'x10.py'
run_python_test '1,2,3,4,5,6 5 3' '[1, 2, 15, 4, 5, 30]'
run_python_test '1,2,3,4,5,6 2 7' '[1, 2, 3, 4, 5, 6]'
end_python_test
