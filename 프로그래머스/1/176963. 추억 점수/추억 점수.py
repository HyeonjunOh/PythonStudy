def solution(name, yearning, photo):
    score = {name[i]: yearning[i] for i in range(len(name))}
    return list(map(lambda x: sum([score[j] for j in x if j in score]), photo))