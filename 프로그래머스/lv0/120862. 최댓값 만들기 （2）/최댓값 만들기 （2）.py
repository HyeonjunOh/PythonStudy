def solution(a):
    a.sort()
    return max(a[0]*a[1], a[-1]*a[-2])