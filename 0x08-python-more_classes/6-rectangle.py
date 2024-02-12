#!/usr/bin/python3

class Rectangle:
    """
        number_of_instances (int): Rectangle instances' numbers.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            width (int): new rectangle width.
            height (int): new rectangle height.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):     #Returns area
        return (self.__width * self.__height)

    def perimeter(self):        #Returns perimeter
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):      #Return rectangle printable presentation
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for k in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if k != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):     #Returns rectangle string representation
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):      #Prints message for every rectangle deletionn
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
