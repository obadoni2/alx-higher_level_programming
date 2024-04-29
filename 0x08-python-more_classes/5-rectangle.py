#!/usr/bin/python3
"""Define a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, heighth=0):
        """Initialize a new Rectangle.
        Args:
          width(int): The width of new retangle.
          height(int):The height of the new rectangle.
          """
          self.width = width
          self.height = height


    @property
    def width(self):
        """Get/set the width of the Rectangle."""
         return self.__width
     
     @width.setter
     def width(self,value):
         if not isinstance(value, int):
             raise TyeError("width must be integar")
         if value < 0:
             raise ValueError("width must be >= 0")
         self. __width = value

    @property
    def heigh(self):
        """ Get/set the height of the Rectangle."""
          return self. __height

    @height.setter
    def height( self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self. __height = value

        def area(self):
            """Return the area of the Rectangle."""
            return (self.__width * self.__height)

      def perimeter(self):
          """"RETURN the perimeter of the Rectangle."""
          if self.__width == 0 or self.__height == 0:
              return (0)
          return((self. __width *2) + (self.__height *2))
      def __str_(self):
          """Return the  printable representation of the Rectangle.
          Represents the rectangle with the #character.
          """

          if self.__width == 0 or self._height == 0:
              return("")

          rect =[]
          for i in range(self.__height):
              [rect.append('#') forn j in range(self.__width)]
              if i != self.__height -1:
                  rect.append("\n")
        return("".join(rect))

    def __del__(self):
        """print a message for every deletion of a REctangle. """
        print("Bye rectangle....")

