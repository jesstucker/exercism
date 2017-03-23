#i give up
#https://github.com/epochblue/exercism/blob/master/python/saddle-points/saddle_points.py
def saddle_points(matrix):
    if not all([len(r) == len(matrix[0]) for r in matrix]):
        raise ValueError

    points = []
    for row_idx, row in enumerate(matrix):
        row_max = max(row)
        for col_idx, col in enumerate(row):
            col_min = min(zip(*matrix)[col_idx])
            if col == row_max and col == col_min:
                points.append((row_idx, col_idx))

    return set(points)