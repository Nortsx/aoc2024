import time


def parse_file_to_2d_dict(file_path):
    with open(file_path, 'r') as file:
        array_coords = [list(line.strip()) for line in file.readlines()]
        result = {}
        for y, line in enumerate(array_coords):
            for x, val in enumerate(line):
                result[(x, y)] = val
        return result

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def fill_area_and_perimeter(start_point, gardens, visited) -> ():
    area_diff = 0
    perimeter_diff = 0
    another_trees = []

    for direction in directions:
        new_point = (start_point[0] + direction[0], start_point[1] + direction[1])
        if new_point not in gardens or gardens[new_point] != gardens[start_point]:
            perimeter_diff += 1

    for direction in directions:
        new_point = (start_point[0] + direction[0], start_point[1] + direction[1])
        if new_point in gardens and gardens[new_point] == gardens[start_point] and new_point not in visited:
            another_trees.append(new_point)
            visited.add(new_point)
            area_diff += 1

    return another_trees, area_diff, perimeter_diff

gardens = parse_file_to_2d_dict('input.txt')

startTime = time.time()

visitedTiles = set()

fence_sum = 0

for key in gardens:
    if key not in visitedTiles:
        perimeter = 0
        area = 1
        visitedTiles.add(key)
        trees_to_visit, calc_area, calc_perimeter = fill_area_and_perimeter(key, gardens, visitedTiles)
        perimeter += calc_perimeter
        area += calc_area
        while len(trees_to_visit) > 0:
            position_to_visit = trees_to_visit.pop()
            new_trees_to_visit, calc_area, calc_perimeter = fill_area_and_perimeter(position_to_visit, gardens, visitedTiles)
            perimeter += calc_perimeter
            area += calc_area
            trees_to_visit.extend(new_trees_to_visit)

        fence_sum += area*perimeter

print(fence_sum)

print("time taken p1:", time.time() - startTime)