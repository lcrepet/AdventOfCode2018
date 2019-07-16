import space

grid = space.Grid()

with open('input.txt') as input_file:
    for line in input_file:
        x, y = line.split(',')
        grid.add_area(int(x), int(y))

nearest_points = 0
for x in range(0, grid.max_x + 1):
    for y in range(0, grid.max_y + 1):
        distances_sum = sum(map(lambda area: area.center.distance_from(x, y), grid.areas))
        if distances_sum < 10000:
            nearest_points += 1

print(nearest_points)

