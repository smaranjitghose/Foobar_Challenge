def solution(entrances, exits, path):
    l_en = len(entrances)
    l_pa = len(path)
    l_ex = len(exits)
    bunn_count = 0
    intermediate_paths = path[l_en:(l_pa-l_ex)]
    for i in range(l_pa - l_en - l_ex):
        sum_range = sum(intermediate_paths[i])
        sum_enter = 0
        for j in entrances:
            sum_enter += path[j][l_en + i]
        bunn_count += min(sum_enter, sum_range)
    return bunn_count