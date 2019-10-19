def is_year_leap(y):
    try:
        y = int(y)
    except (ValueError, TypeError):
        return None
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


def triangle(x, y, z):
    try:
        x, y, z = float(x), float(y), float(z)
    except (ValueError, TypeError):
        return None
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False


def triangle_plus(x, y, z):
    try:
        x, y, z = float(x), float(y), float(z)
    except (ValueError, TypeError):
        return None
    if x == y == z and triangle(x, y, z):
        return "Equilateral triangle"
    elif (x == y != z or x != y == z or x == z != y) and triangle(x, y, z):
        return "Isosceles triangle"
    elif triangle(x, y, z):
        return "Versatile triangle"
    else:
        return "Not a triangle"


if __name__ == '__main__':
    print("""is_year_leap("2000")""", is_year_leap("2000"))
    print("""is_year_leap(/"dfd/")""", is_year_leap("dfd"))
    print("is_year_leap(2000)", is_year_leap(2000))
    print("is_year_leap(3)", is_year_leap(3))
    print("is_year_leap(-3.4)", is_year_leap(-3.4))

    print("triangle(0, 1, 1)", triangle(0, 1, 1))
    print("triangle(1, -2, 2)", triangle(1, -2, 2))
    print("triangle(1, 2, 2.5)", triangle(1, 2, 2.5))

    print("triangle_plus(0, 0, 0)", triangle_plus(0, 0, 0))
    print("triangle_plus(-1, 1, 1)", triangle_plus(-1, 1, 1))
    print("triangle_plus(1, 1, 1)", triangle_plus(1, 1, 1))
    print("triangle_plus(1, 2, 2)", triangle_plus(1, 2, 2))
    print("triangle_plus(1, 2, 2.5)", triangle_plus(1, 2, 2.5))
    print("triangle_plus(1, 2, 3)", triangle_plus(1, 2, 3))
