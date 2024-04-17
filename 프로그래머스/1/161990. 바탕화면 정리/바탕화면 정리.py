def solution(wallpaper):
    x = []
    y = []
    for r_idx, row in enumerate(wallpaper):
        for c_idx, col in enumerate(row):
            if col == "#":
                x.append(r_idx)
                y.append(c_idx)
    return [min(x), min(y), max(x)+1, max(y)+1]