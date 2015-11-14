#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'sum.py'
run_python_test '1,3,5,7,9' '25'
run_python_test '0,0,0' '0'
run_python_test '-2,-2,-2' '-6'
end_python_test
