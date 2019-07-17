EMPTY_CELL = ''
MULTIPLE_CLAIMS_CELL = 'X'

class Claim:
    """
    Represents a claim made by elves about how to cut the fabric.
    """

    def __init__(self, id, x, y, height, width):
        self.id = id
        self.point = Point(x, y)
        self.height = height
        self.width = width
        self.is_overlapped = False

    def print_on(self, plan):
        """
        Try to print the claimed area on a plan to check if there are
        overlapped parts.

        :param plan: Plan of the fabric with some claimed areas already
        printed on
        :type plan: list(list(str))
        :rtype: int
        """

        overlapped_cells = 0

        for i in range(self.point.y, self.point.y + self.height):
            for j in range(self.point.x, self.point.x + self.width):
                if plan[i][j] == EMPTY_CELL:
                    plan[i][j] = self.id
                elif not(plan[i][j] == MULTIPLE_CLAIMS_CELL):
                    plan[i][j] = MULTIPLE_CLAIMS_CELL
                    overlapped_cells += 1
                    self.is_overlapped = True

        return overlapped_cells

    def check_if_overlapped_on(self, plan):
        """
        Check if the claimed area is overlapped by another.

        :param plan: Plan of the fabric with all the claimed areas printed on
        :type plan: list(list(str))
        :rtype: bool
        """

        for i in range(self.point.y, self.point.y + self.height):
            for j in range(self.point.x, self.point.x + self.width):
                if plan[i][j] == MULTIPLE_CLAIMS_CELL:
                    self.is_overlapped = True

        return self.is_overlapped



class Point:
    """
    Allows to store coordinates on 2D plans.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
