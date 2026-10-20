"""Reusable geometry functions for the custom module calculator."""

import math


def rectangle_area(length, breadth):
    if length < 0 or breadth < 0:
        raise ValueError("Length and breadth cannot be negative.")
    return length * breadth


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius * radius
