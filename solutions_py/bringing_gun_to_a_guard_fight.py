def solution(dimensions, your_position, guard_position, distance):
    cx, cy = your_position
    sqr_dist = distance ** 2

    if your_position == guard_position:
        return 0

    def get_mirrored(node):
        yield (node[0], node[1] - 2 * (node[1] - dimensions[1]))
        yield (node[0], -node[1])
        yield (node[0] - 2 * (node[0] - dimensions[0]), node[1])
        yield (-node[0], node[1])

    def get_slope(dx, dy):
        if dx == dy == 0:
            return (0, 0)
        tx, ty = abs(dx), abs(dy)
        while ty:
            tx, ty = ty, tx % ty
        return (dx // tx, dy // tx)

    def get_all_mirror(node):
        prev = mirrors = set([(node[0], node[1])])
        while True:
            new_mirrors = set()
            for node in prev:
                for tmp in get_mirrored(node):
                    if (cx - tmp[0]) ** 2 + (cy - tmp[1]) ** 2 > sqr_dist:
                        continue
                    new_mirrors.add(tmp)
            new_mirrors -= mirrors
            if not new_mirrors:
                break
            mirrors |= new_mirrors
            prev = new_mirrors
        return mirrors

    guard = get_all_mirror(guard_position)
    your = get_all_mirror(your_position)
    your_slope = {}

    for x, y in your:
        dx = cx - x
        dy = cy - y
        dist = dx ** 2 + dy ** 2
        slope = get_slope(dx, dy)
        if dist <= your_slope.get(slope, sqr_dist):
            your_slope[slope] = dist

    ans = set()
    for x, y in guard:
        dx = cx - x
        dy = cy - y
        dist = dx ** 2 + dy ** 2
        slope = get_slope(dx, dy)
        if dist <= your_slope.get(slope, sqr_dist):
            ans.add(slope)
    return len(ans)
    
    
    