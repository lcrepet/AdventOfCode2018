import math
import space

grid = space.Grid()

with open('input.txt') as input_file:
    for line in input_file:
        x, y = line.split(',')
        grid.add_area(int(x), int(y))

for x in range(0, grid.max_x + 1):
    for y in range(0, grid.max_y + 1):
        previous_nearest = None
        nearest_area = None
        previous_min = math.inf
        min_distance = math.inf

        for area in grid.areas:
            distance = area.center.distance_from(x, y)

            if distance <= min_distance:
                previous_min = min_distance
                min_distance = distance
                previous_nearest = nearest_area
                nearest_area = area

        if not(previous_min == min_distance):
            nearest_area.add_point(grid.is_on_border(x, y))

largest_area = max(list(filter(lambda area: not(area.is_infinite), grid.areas)), key=lambda area: area.size)
print(largest_area.size)


