def checkStraightLine(coordinates):
    if len(coordinates) < 3:
        return True

    x0, y0 = coordinates[0]
    dx0, dy0 = coordinates[1][0] - x0, coordinates[1][1] - y0

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        dx, dy = x - x0, y - y0

        if dx0 * dy != dy0 * dx:
            return False

    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))  # Output: True
