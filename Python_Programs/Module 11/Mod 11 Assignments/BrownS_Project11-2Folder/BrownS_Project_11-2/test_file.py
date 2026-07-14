#!/usr/bin/env python3
#
# Problem: Customer Class Unit Test
# Files: BrownS_CustomerClassUnitTest.py
#
# Author: Samuel Brown
# Date: 3 April 2026

#Importing pytest module and the file class
import pytest

from BrownS_CustomerClassUnitTest import Customer
@pytest.fixture
def test_fixture_function():
    CustomerData = Customer(101, "Sam", "Brown", "BrownCompany", "1234 Brown St.", "Brownville", "BrownState", "1020")
    return CustomerData

def test_id(test_fixture_function):
    #Check the ID is correct
    assert test_fixture_function.id == 101

def test_without_output_address(test_fixture_function):
    #Check the ID is correct
    Address = test_fixture_function.full_address()
    assert Address == "BrownCompany\n1234 Brown St.\nBrownville, BrownState 1020"

def test_with_output_address(test_fixture_function):
    #Check the ID is correct
    Address = test_fixture_function.partial_address()
    assert Address == "1234 Brown St.\nBrownville, BrownState 1020"

def test_first_name(test_fixture_function):
    #Check the ID is correct
    assert test_fixture_function.firstName == "Sam"
    
def test_last_name(test_fixture_function):
    #Check the ID is correct
    assert test_fixture_function.lastName == "Brown"