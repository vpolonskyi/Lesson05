import math

class Room:
    """
    Class desc
    """
    def __init__(self, x: float = 1, y: float = 1):
        self.x = x
        self.y = y

    def area(self):
        return x * y

    def perimeter(self):
        return 2 * x + 2 * y

class Point:
    """
    Class desc
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to_point(self, args):
        return ((self.x - args.x) ** 2 + (self.y - args.y) ** 2) ** 0.5

    def __str__(self):
        return f"{self.__class__} object: name: {self.x} {self.y}"

    def __iter__(self):
        return iter([self.x, self.y])

    def dec_to_sf(self):
        """
        https://ru.wikipedia.org/wiki/%D0%A1%D1%84%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82
        :return:
        """
        r = self.distance_to_zero()
        fi = math.atan2(self.y, self.x)
        return r, fi


if __name__ == '__main__':
    a = Point(10, 10)
    b = Point(3, -4)
    print(a.distance_to_zero())
    print(a.distance_to_point(b))
    print(a.dec_to_sf())
