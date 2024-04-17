#!/usr/bin/python3
"""the rectangle class for instantiaion

Returns:
    str: from the str
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """initializes the instance of the class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """handles the print

        Returns:
            str: custom str
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
