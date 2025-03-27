'''area module'''

def circle(radius):
    """Calculate the area of a circle given its radius."""
    return 3.14 * radius ** 2

def square(side):
    """Calculate the area of a square given the length of its side."""
    return side ** 2

def rectangle(length, breadth):
    """Calculate the area of a rectangle given its length and breadth."""
    return length * breadth

def parallelogram(base, height):
    """Calculate the area of a parallelogram given its base and height."""
    return base * height

def triangle(base, height):
    """Calculate the area of a triangle given its base and height."""
    return 1/2 * (base * height)
