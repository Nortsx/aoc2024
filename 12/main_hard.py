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

angles = [180, 0, 90, 270]


def fill_area_and_fence(start_point, gardens, visited, fences) -> ():
    area_diff = 0
    another_trees = []

    for idx, direction in enumerate(directions):
        new_point = (start_point[0] + direction[0], start_point[1] + direction[1])
        if new_point not in gardens or gardens[new_point] != gardens[start_point]:
            fences.add((new_point, angles[idx]))

    for direction in directions:
        new_point = (start_point[0] + direction[0], start_point[1] + direction[1])
        if new_point in gardens and gardens[new_point] == gardens[start_point] and new_point not in visited:
            another_trees.append(new_point)
            visited.add(new_point)
            area_diff += 1

    return another_trees, area_diff


def find_side(fence_side, fences, visited, angle) -> []:
    while True:
        prev_len = len(fence_side)
        positionLeft = fence_side[0]
        positionRight = fence_side[-1]
        left_side = (positionLeft[0] + fence_directions[angle][1][0], positionLeft[1] + fence_directions[angle][1][1])
        right_side = (positionRight[0] + fence_directions[angle][0][0], positionRight[1] + fence_directions[angle][0][1])
        if (left_side, angle) in fences and (left_side, angle) not in visited:
            fence_side = [left_side] + fence_side
            visited.add((left_side, angle))
        if (right_side, angle) in fences and (right_side, angle) not in visited:
            fence_side.append(right_side)
            visited.add((right_side, angle))
        if len(fence_side) == prev_len:
            break

    return fence_side

gardens = parse_file_to_2d_dict('input.txt')

startTime = time.time()

visitedTiles = set()

fence_sum = 0

fence_directions = {0: [(1, 0), (-1, 0)], 180: [(1, 0), (-1, 0)] , 90: [(0, 1), (0, -1)], 270: [(0, 1), (0, -1)]}


for key in gardens:
    if key not in visitedTiles:
        fences = set()
        visited_fences = set()
        area = 1
        visitedTiles.add(key)
        trees_to_visit, calc_area = fill_area_and_fence(key, gardens, visitedTiles, fences)
        area += calc_area
        while len(trees_to_visit) > 0:
            position_to_visit = trees_to_visit.pop()
            new_trees_to_visit, calc_area = fill_area_and_fence(position_to_visit, gardens, visitedTiles, fences)
            area += calc_area
            trees_to_visit.extend(new_trees_to_visit)

        sides = 0
        sides_to_visit = []

        for fence in fences:
            if fence not in visited_fences:
                visited_fences.add(fence)
                side_list = find_side([fence[0]], fences, visited_fences, fence[1])
                sides += 1

        fence_sum += area*sides

print(fence_sum)

print("time taken p2:", time.time() - startTime)