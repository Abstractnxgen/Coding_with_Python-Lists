#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'populate.py'
run_python_test '0' '[]'
run_python_test '1' '[0]'
run_python_test '-2' '[]'
run_python_test '8' '[0, 10, 20, 30, 40, 50, 60, 70]'
end_python_test
