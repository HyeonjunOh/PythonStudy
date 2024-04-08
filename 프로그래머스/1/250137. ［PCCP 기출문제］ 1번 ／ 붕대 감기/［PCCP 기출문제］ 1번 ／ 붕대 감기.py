def solution(bandage, health, attacks):
    attacks = [[0, 0]] + attacks
    cur_health = health
    for i in range(len(attacks)-1):
        idle = attacks[i+1][0] - attacks[i][0] - 1
        a, b = divmod(idle, bandage[0])
        heal = bandage[2]*a + idle*bandage[1]
        cur_health = min(cur_health + heal, health)
        cur_health -= attacks[i+1][1]
        if cur_health <= 0:
            return -1
    return cur_health