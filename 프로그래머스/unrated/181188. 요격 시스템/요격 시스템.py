def solution(targets):
    result = 0
    targets.sort()
    rx = targets[0][1]
    for s, e in targets[1:]:
        if s < rx:
            if e < rx:
                rx = e
        else:
            rx = e
            result += 1
    return result + 1