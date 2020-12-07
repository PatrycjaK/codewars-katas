# Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c):
    if max(a, b, c) == a and b + c > a:
        return True
    elif max(a, b, c) == b and a + c > b:
        return True
    elif max(a, b, c) == c and a + b > c:
        return True
    else:
        return False
