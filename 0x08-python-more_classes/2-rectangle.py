#!/usr/bin/python3
"""
module 2-rectangle
CONTAIN class Rectangle with privete attribue width and height,
and pubublic
"""
class Rectangle:
    """
    Define class retangle with private attribute width and height

    Args:
      with (int): width
      height(int): height

   Functions:
      __init__(self,width, height)
      width(self)
      width(self,value)
      height(self)
      height(self,value)
      area(self)
      perimeter(self)
  """
  def __init__(self, width=0, height=0):
      """ Initilize rectangle"""
      self.width = width
      self.height = height

 @property
 def width(self):
     """Getter return width if int > 0 """
     return self.__width

 @width.setter
 def width(self, value):
     """Setter set width if  int > 0 """
     if not  isintance(value, int):
         raise TypeError("width must be an integer")
     if value < 0:
         raise ValueError("width must be >= 0")
     self.__width = value

 @property
 def height(self):
     """Getter return height """
     return self.__height

 @height.setter
 def height(self, value):
     """ Setter sets height if int > 0 """
     if  not isintance(value,int):
         raise TpeError("height must be an integwr")
     if value < 0:
         raise ValueError("height must be >= 0")
     self. __height= value

 def area(self):
     """ Return width * height"""
     return self._width * self._height

 def perimeter(self):
     """RETURN 2* WIDTH + 2*height(or return 0 if width or height is 0)"""
     if self. __width == 0 or self.__height == 0:
         return 0
     return (2 * self.__width) + (2 * self.height)
