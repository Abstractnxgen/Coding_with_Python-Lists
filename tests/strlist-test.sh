#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'strlist.py'
run_python_test '' "['AAA', 'BBB', 'CCC']"
end_python_test
#
#
#

