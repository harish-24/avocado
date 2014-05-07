# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2013-2014
# Author: Lucas Meneghel Rodrigues <lmr@redhat.com>

"""
Exception classes, useful for tests, and other parts of the framework code.
"""


class JobBaseException(Exception):

    """
    The parent of all job exceptions.
    """
    status = "NEVER_RAISE_THIS"


class JobError(Exception):

    """
    A generic error happened during a job execution.
    """
    status = "ERROR"


class TestBaseException(Exception):

    """
    The parent of all test exceptions.
    """
    status = "NEVER_RAISE_THIS"


class TestSetupFail(TestBaseException):

    """
    Indicates an error during a setup procedure.
    """
    status = "ERROR"


class TestError(TestBaseException):

    """
    Indicates that something went wrong with the test harness itself.
    """
    status = "ERROR"


class TestNAError(TestBaseException):

    """
    Indictates that the test is Not Applicable.

    Should be thrown when various conditions are such that the test is
    inappropriate. For example, inappropriate architecture, wrong OS version,
    program being tested does not have the expected capability (older version).
    """
    status = "TEST_NA"


class TestFail(TestBaseException):

    """
    Indicates that the test failed. The test job will continue, though.
    """
    status = "FAIL"


class TestWarn(TestBaseException):

    """
    Indicates that bad things (may) have happened, but not an explicit
    failure.
    """
    status = "WARN"


class CmdError(Exception):

    def __init__(self, command, result):
        self.command = command
        self.result = result

    def __str__(self):
        if self.result.exit_status is None:
            msg = "Command '%s' failed and is not responding to signals"
            msg %= self.command
        else:
            msg = "Command '%s' failed (rc=%d)"
            msg %= (self.command, self.result.exit_status)
        return msg
