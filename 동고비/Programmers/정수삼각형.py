def solution(t_list):
    for i in range(1, len(t_list)):
        for j in range(i+1):
            if j == 0:
                t_list[i][j] = t_list[i][j] + t_list[i-1][j]
            elif i == j:
                t_list[i][j] = t_list[i][j] + t_list[i-1][j-1]
            else:
                t_list[i][j] = max(t_list[i][j]+t_list[i-1][j],
                                   t_list[i][j]+t_list[i-1][j-1])

    return max(t_list[-1])