from collections import deque

def solution(bandage, health, attacks):
    band_t, heal, bonus_heal = bandage
    cur_health = health
    l = attacks[-1][0]
    attacks = deque(attacks)
    next_atk = 0
    continued = 0
    for i in range(l):
        if next_atk == 0:
            next_atk = attacks.popleft()
        if i+1 == next_atk[0]:
            cur_health -= next_atk[1]
            if cur_health <= 0:
                return -1
            next_atk = 0
            continued = 0
        else:
            if cur_health == health:
                continued = 0
            else:
                cur_health = min(cur_health + heal, health)
                continued += 1
                if continued == band_t:
                    cur_health = min(cur_health + bonus_heal, health)
                    continued = 0
    return cur_health