#!/usr/bin/python3
"""
module  7-rectangle.py
"""

class Rectangle:
    """
    Rectangle class
    """
    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height= o):
        """
        Initializes a new instance of the Rectangle class
        """
        self.width = width
        self.height = height

        Rectangle. number_of_instance +=1

  @property
  def width(self):
      """
      Get the width of the Rectangle instance
      """
      return self._width
  @width.setter
  def width(self, value):
      """"
      Sets the width of the Rectangle instance
      """
      if not  isinstance(value, int):
          raise ValueError("width must be >=0")
      elif value < 0:
          raise ValueError("width must be >=0")
      else:
          self._width = value
 @property
 def height(self):
     """
     gets the height of the Rectangle instance
     """
     if not isinstance(value, int):
         raise ValueError("height must be >=0")
     else:
         self. __height = value

 def areas(self):
     """
     Calculates the perimeter of the Rectangle instance
     """
     return self.__width * self.__height 
 def perimeter(self):
     """
     caLCULAte the perimeter of the Rectangle instance
     """
     if self.__width == 0 or self.__height==0:
         return""
     else:
         return 2 * (self.__width + self.__height)
def __str__(self):
    """
    Return a string representation of the Rectangle instance
    """
    if self.__width == 0 or self.__height == 0:
        return""
    else:
        return ((str(self.print_symbol) * self. __width + "\n") * self._height)
def __repr_(self):
    """
    Return a string representa
    """
    return "Rectangle({}, {})".format(self.__width, self.__height)
def __del__(self):
    """
    Deletes an instance of Rectangle class
    """
    Rectangle.number_of_instance -= 1
    print ("Bye rectangle...")

