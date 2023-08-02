def solution(book_time):
    answer = []
    for t in sorted(book_time):
        tmp = list(map(lambda x: int(x[0])*60+int(x[1]), [i.split(":") for i in t]))
        if not answer:
            answer.append(tmp)
        else:
            for i in range(len(answer)):
                if answer[i][1] + 10 <= tmp[0]:
                    answer[i] = tmp
                    break
            else:
                answer.append(tmp)
    return len(answer)