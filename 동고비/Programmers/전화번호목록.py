def solution(phone_book):
    phone_book.sort()
    answer = True
    stop = False
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            l = len(phone_book[i])
            if phone_book[i] == phone_book[j][:l]:
                answer = False
                stop = True
        if stop:
            break
    return answer