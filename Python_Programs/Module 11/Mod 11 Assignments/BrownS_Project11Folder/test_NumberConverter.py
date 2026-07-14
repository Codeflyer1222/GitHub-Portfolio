#!/usr/bin/env python3
#
# Problem: Number Converter Unit Test
# Files: BrownS_NumberConverterUnitTest
#
# Author: Samuel Brown
# Date: 3 April 2026

#Import modules
import pytest
from BrownS_NumberConverterUnitTest import converter

#Series of tests for the converter function
def test_one():
    assert converter('9999') == "9999 is nine thousand nine hundred ninety-nine"

def test_two():
    assert converter('-9999') == "-9999 is negative nine thousand nine hundred ninety-nine"

def test_three():
    assert converter('0') == "0 is zero"

def test_four():
    assert converter('1100') == "1100 is one thousand one hundred "

def test_five():
    assert converter('100') == "100 is one hundred "

def test_six():
    assert converter('9000') == "9000 is nine thousand "

def test_seven():
    assert converter('2001') == "2001 is two thousand one"