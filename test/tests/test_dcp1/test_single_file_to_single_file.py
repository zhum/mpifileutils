#!/usr/bin/env python2
from subprocess import call

def test_dcp1_single_file_to_single_file():
        rc = call("~/fileutils.git/test/legacy/dcp1_tests/test_dcp1_single_file_to_single_file/test.sh", shell=True)
