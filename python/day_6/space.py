class Grid:
    """
    Represents the 2D map with all the areas in space
    """

    def __init__(self):
        self.areas = []
        self.max_x = 0
        self.max_y = 0

    def add_area(self, x, y):
        """
        Add a new area to the grid.

        When a new area is added, borders values can be updated if the new
        area is "out" the current grid.

        :param x: coordinate of the center of the new area on x-axis
        :param y: coordinate of the center of the new area on y-axis
        """

        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        self.areas.append(Area(x, y))

    def is_on_border(self, x, y):
        """
        Allow to know if a given space is on the border of the current
        grid.

        :param x: coordinate of the point on x-axis
        :param y: coordinate of the point on y-axis
        :rtype: bool
        """
        return x == 0 or y == 0 or x == self.max_x or y == self.max_y


class Area:
    """
    Set of points defined by its center.
    """
    def __init__(self, center_x, center_y):
        self.center = Point(center_x, center_y)
        self.size = 0
        self.is_infinite = False

    def add_point(self, on_border):
        """
        Increment the number of points in the area

        If the given point is on the grid's border, the area is called "infinite".

        :param on_border: specify if the added point is on the grid's border
        :type on_border: bool
        """

        self.size += 1
        self.is_infinite = self.is_infinite or on_border


class Point:
    """
    Point in space, defined by x-axis and y-axis coordinates.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, x, y):
        """
        Compute Manhattan distance between two points.

        :param x: coordinate of the other point on x-axis
        :param y: coordinate of the other point on y-axis
        """

        return abs(self.x - x) + abs(self.y - y)
