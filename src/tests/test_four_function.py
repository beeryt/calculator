import pytest
from calculator import Calculator

def testInput():
	c = Calculator()
	assert c.input("1")			== "1"
	assert c.input("1 1")		== "111"
	assert c.input('=')			== "111."
	assert c.input("4")			== "4"

def testAddition():
	c = Calculator()
	assert c.input("1 + 1 =")	== "2."
	assert c.input("1 + - 2 =")	== "-1."
	assert c.input("5 + 0 =")	== "5"

def testSubtraction():
	c = Calculator()
	assert c.input("1 - 1 =")	== "0."
	assert c.input("0 - 1 =")	== "-1."
	assert c.input("2 - 1 =")	== "1."

def testMultiply():
	c = Calculator()
	assert c.input("2 * 3 =")	== "6."