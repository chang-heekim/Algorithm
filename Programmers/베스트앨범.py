import collections

def solution(genres, plays):
    storage = -1
    genre_lst = list(collections.Counter(genres).keys()) 
    num = len(collections.Counter(genres))
    play_lst = list(zip(plays, genres))
    count_lst = []
    answer = []
    for idx in range(num):
        count = 0
        for i in range(len(play_lst)):
            if genre_lst[idx] == play_lst[i][1]:
                count += play_lst[i][0] 
        count_lst.append(count)

    total_count = {genre : count for genre, count in zip(genre_lst, count_lst)}
    sequence = sorted(total_count.items(), key=lambda x : x[1], reverse=True)          
    for seq in sequence:
        index_idx=0
        cnt = 0
        for i in range(len(play_lst)):
            if sorted(play_lst, reverse=True)[i][1] == seq[0]:
                if play_lst.index(sorted(play_lst, reverse=True)[i]) == storage:
                    index = list(filter(lambda x: play_lst[x] == sorted(play_lst, reverse=True)[i], range(len(play_lst))))
                    index_idx += 1
                    answer.append(index[index_idx])
                else:
                    answer.append(play_lst.index(sorted(play_lst, reverse=True)[i]))
                    
                storage = play_lst.index(sorted(play_lst, reverse=True)[i])
                
                cnt += 1
                if cnt == 2:
                    cnt = 0
                    break
                    
    return answer