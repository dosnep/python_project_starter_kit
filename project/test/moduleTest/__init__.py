import unittest

from project.test.moduleTest.module_test import ModuleTest


def moduleTestBuilder():
    testChainsBuilder = unittest.TestSuite()
    testsChainsObject = [ModuleTest("test_message")]

    for obj in testsChainsObject:
        testChainsBuilder.addTest(obj)

    return testChainsBuilder
