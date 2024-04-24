#!/usr/bin/python3
"""DEFINE A RECTANGLE CLASS."""
 class Rectangle:
     """"REpresent a rectangle."""
     def __init__(self, width=o, height=0):
         """Initialize a new RECTANGLE.
        Args:
        width (int): The widthnof the new rectangle.
        height (init): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
    @width. setter
    def width(self, value):
        if not isinstance(value, int):
            raise TyeError("width must be >= 0")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def heigh(self):
            """"Get/set the height of the Rectangle. """
            return self.__height

        @height. setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            raise.ValueError("height must be >= 0")
            self. __height = value


      def area(self):
          """" Return the area of the Rectangle."""
          return(self.__width * self.__height)

          if self. __width == 0 or self. __height ==0:
              return (0)
          return ((self. __width *2) + (self.__height  *2))

