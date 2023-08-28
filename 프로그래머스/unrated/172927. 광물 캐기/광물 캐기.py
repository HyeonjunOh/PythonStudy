import heapq
import math

def get_fat(pick, minerals):
    return sum([math.ceil(i/pick) for i in minerals])

def solution(picks, minerals):
    result = 0
    heap = []
    fatigue = {"diamond": 25, "iron": 5, "stone": 1}
    minerals = [fatigue[i] for i in minerals]
    for i in range(sum(picks)):
        tmp = minerals[i*5:(i+1)*5]
        if not tmp:
            break
        heapq.heappush(heap, (-sum(tmp), len(tmp), tmp))
    while heap:
        tmp = heapq.heappop(heap)[2]
        print(picks, tmp)
        if picks[0]:
            result += get_fat(25, tmp)
            picks[0] -= 1
        elif picks[1]:
            result += get_fat(5, tmp)
            picks[1] -= 1
        else:
            result += get_fat(1, tmp)
            picks[2] -= 1
    return result