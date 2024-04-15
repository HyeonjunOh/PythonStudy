def solution(players, callings):
    rank = {j: i for i, j in enumerate(players)}
    for call in callings:
        idx = rank[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        rank[players[idx]], rank[players[idx-1]] = idx, idx-1
    return players