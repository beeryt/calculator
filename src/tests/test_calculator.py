import pytest
from calculator import Calculator

def testSquareArea():
  """Find the area of a square room with sides measuring 15 Feet 8-1/2 Inches."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("1 5 Feet 8 Inch 1 / 2")         == "15 ft 8-1/2 in"
  assert c.input("Conv %")                        == "246.7517 sq ft"

def testSquareRoot():
  """What is the Square Root of 200?"""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("2 0 0 Conv .")                  == "14.14214"

def testSquareCubicWasteAllowance():
  """Add a 10% waste allowance to 55 Square Feet. Then add a 20% waste allowance to 150 Cubic Feet."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("5 5 Feet Feet + 1 0 %")         == "60.5 sq ft"
  assert c.input("1 5 0 Feet Feet Feet + 2 0 %")  == "180. cu ft"

def testLinearConversions():
  """Convert 10 Feet 6 Inches to other dimensions, including Metric."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0." 
  assert c.input("1 0 Feet 6 Inch")               == "10 ft 6 in"
  assert c.input("Conv Yds")                      == "3.5 yd"
  assert c.input("Conv Inch")                     == "126 in"
  assert c.input("Conv 5")                        == "3.200 m"
  assert c.input("Conv 7")                        == "320.04 cm"
  assert c.input("Conv 9")                        == "3200.4 mm"

def testConvertDecimalFeet():
  """Convert 14 Feet 7-1/2 Inches to Decimal Feet."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("1 4 Feet 7 Inch 1 / 2")         == "14 ft 7-12 in"
  assert c.input("Conv Feet")                     == "14.625 ft"

def testConvertFeetInches():
  """Convert 22.75 Feet to Feet-Inches."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("2 2 . 7 5 Feet")                == "22.75 ft"
  assert c.input("Conv Feet")                     == "22 ft 9 in"

def testSquareCubicConversions():
  """Convert 14 Square Feet to Square Yards."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("1 4 Feet Feet")                  == "14 sq ft"
  assert c.input("Conv Yds")                      == "1.555556 sq yd"

def testConvertYardFeet():
  """Convert 25 sq yds to sq ft."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("2 5 Yds Yds")                   == "25 sq yd"
  assert c.input("Conv Feet")                     == "225 sq ft"

def testConvertCubicFeetYard():
  """Convert 12 cu ft to cu yd."""
  c = Calculator()
  assert c.input("On/C On/C")                     == "0."
  assert c.input("1 2 Feet Feet Feet")            == "12 cu ft"
  assert c.input("Conv Yds")                      == "0.444444 cu yd"

def testMemory():
  c = Calculator()
  assert c.input("3 5 5 M+")  == "M+ 355."          and c.memory == True
  assert c.input("2 5 5 M+")  == "M+ 255."          and c.memory == True
  assert c.input("7 4 5 M-")  == "M- 745."          and c.memory == True
  assert c.input("Rcl M+")    == "TTL stored -135." and c.memory == True
  assert c.input("M+")        == "AVG -45"          and c.memory == True
  assert c.input("M+")        == "Cnt 3"            and c.memory == True
  assert c.input("Rcl Rcl")   == "M+ -135."         and c.memory == False

def testProjectPaintUnits():
  """How many quarts of paint will you need to cover a wall measuring 12 ft x 8 ft? How many Pints? How many Gallons?"""
  c = Calculator()
  assert c.input("On/C On/C")             == "0."
  assert c.input("1 2 Feet x 8 Feet =")   == "96. sq ft"
  assert c.input("Paint")                 == "QT 1.10"
  assert c.input("Paint")                 == "PINT 2.19"
  assert c.input("Paint")                 == "GAL 0.27"

def testProjectTilesNumber():
  """How many tiles do you need to cover a floor measuring 10ft x 15ft? You want a grout width of 1/8 in, but you're not sure of the tile size you're going to use. So, find the number of tiles in various sizes. Also, add a 10% waste allowance, in case you need extra tile."""
  c = Calculator()
  assert c.input("1 / 8 Stor Tile")       == "GRT stored 0-1/8 in"
  assert c.input("1 0 Feet x 1 5 Feet =") == "150. sq ft"
  assert c.input("+ 1 0 %")               == "165. sq ft"
  assert c.input("Tile")                  == "TILE 72.33 (18 in)"
  assert c.input("Tile")                  == "TILE 91.38 (16 in)"

def testProjectCustomTileSize():
  """How many tiles do you need if you're using a custom tile size of 4-1/4 Inches x 4-1/4 Inches to cover a floor that is 10 Feet x 15 Feet?"""
  c = Calculator()
  assert c.input("4 Inch 1 / 4 x 4 Inch 1 / 4 = Store CustomTile")        \
                                          == "TILE stored 18.0625 sq in"
  assert c.input("10 Feet x 15 Feet =")   ==  "150. sq ft"
  assert c.input("CustomTile")            == "TILE 1195.85"
