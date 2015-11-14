#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'numsearch.py'
run_python_test '1,3,11,42,12 2' '-1'
run_python_test '"" 1' '-1'
run_python_test '1,3,11,42,12 42' '3'
end_python_test
