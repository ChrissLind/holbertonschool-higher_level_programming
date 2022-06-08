#!/usr/bin/python3
"""Defines a Rectangle model class"""
from models.base import Base


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initalizes a new rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__('id')

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Get/set the height of the Rectangle"""
        return self.__height

    @property
    def x(self):
        """Get/set the x coordinate of the Rectangle"""
        return self.__x

    @property
    def y(self):
        """Get/set the y coordinate of the Rectangle"""
        return self.__y
