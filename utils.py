def convert_coords(coords):
    x, y = coords
    PITCH_LENGTH = 106
    PITCH_WIDTH = 68

    if x is None or y is None:
        return None, None

    x_m = (x / 100) * PITCH_LENGTH - PITCH_LENGTH / 2
    y_m = PITCH_WIDTH / 2 - (y / 100) * PITCH_WIDTH

    return (x_m, y_m)

def get_center(box):
    xs = [p[0] for p in box]
    ys = [p[1] for p in box]
    
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    cx = round((min_x + max_x) / 2, 1)
    cy = round((min_y + max_y) / 2, 1)

    return (cx, cy)

def get_quadrant(coords, zone, mapping):
    x, y = coords
    box = mapping[str(zone)]

    xs = [p[0] for p in box]
    ys = [p[1] for p in box]
    
    min_x, max_x = min(xs), max(xs)
    max_y, min_y = max(ys), min(ys)

    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2

    if x <= cx and y >= cy:
        return 1
    elif x > cx and y >= cy:
        return 2
    elif x <= cx and y < cy:
        return 3
    else:
        return 4