#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'max.py'
run_python_test '1,5,8,23,78,22,0' '4'
run_python_test '1,1,1,1,1' '0'
run_python_test '1,1,1,1,2' '4'
end_python_test
