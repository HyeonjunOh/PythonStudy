def solution(friends, gifts):
    giftness = {friend: 0 for friend in friends}
    history = {}
    next_month = {friend: 0 for friend in friends}

    for gift in gifts:
        g, r = gift.split()
        giftness[g] += 1
        giftness[r] -= 1
        if gift in history:
            history[gift] += 1
        else:
            history[gift] = 1
            
    for i in range(len(friends) - 1):
        for j in range(i+1, len(friends)):
            itoj = history.get(friends[i] + " " + friends[j])
            jtoi = history.get(friends[j] + " " + friends[i])

            if (itoj is None and jtoi is None) or (itoj == jtoi):
                if giftness[friends[i]] > giftness[friends[j]]:
                    next_month[friends[i]] += 1
                elif giftness[friends[i]] < giftness[friends[j]]:
                    next_month[friends[j]] += 1
            elif itoj is None:
                next_month[friends[j]] += 1
            elif jtoi is None:
                next_month[friends[i]] += 1
            else:
                if itoj < jtoi:
                    next_month[friends[j]] += 1
                elif itoj > jtoi:
                    next_month[friends[i]] += 1

    return max(next_month.values())