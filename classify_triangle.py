import math

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on its side lengths.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.

    Returns:
        str: Type of the triangle (e.g., "Equilateral Triangle", "Isosceles Triangle", 
             "Scalene Triangle", "Invalid Triangle").
    """

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Triangle"

    sides = sorted([a, b, c])
    a, b, c = sides

    if a + b <= c:
        return "Invalid Triangle"

    is_right = math.isclose(a**2 + b**2, c**2)

    if a == b == c:
        return "Equilateral Triangle"
    if a == b or b == c:
        return "Isosceles Triangle and Right" if is_right else "Isosceles Triangle"
    return "Scalene Triangle and Right" if is_right else "Scalene Triangle"

if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(5, 5, 5))
    print(classify_triangle(2, 2, 3))
    print(classify_triangle(7, 24, 25))
    print(classify_triangle(1, 1, 2))
    print(classify_triangle(-3, 4, 5))
    print(classify_triangle(0, 4, 5))
    