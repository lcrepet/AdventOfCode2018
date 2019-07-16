class Grid:
    def __init__(self):
        self.areas = []
        self.max_x = 0
        self.max_y = 0

    def add_area(self, x, y):
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        self.areas.append(Area(x, y))

    def is_on_border(self, x, y):
        return x == 0 or y == 0 or x == self.max_x or y == self.max_y


class Area:
    def __init__(self, center_x, center_y):
        self.center = Point(center_x, center_y)
        self.size = 0
        self.is_infinite = False

    def add_point(self, on_border):
        self.size += 1
        self.is_infinite = self.is_infinite or on_border


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, x, y):
        return abs(self.x - x) + abs(self.y - y)
