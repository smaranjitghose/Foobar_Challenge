def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    queue = [source]
    while len(queue) > 0:
        top = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[top][i][1] - matrix[top][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    # Get route
                    visited[destination] = top
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    # Get flow value and update augmented graph
                    temp = 1
                    total = float("inf")
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        cur = path[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        if entry[1] < 0: # Already augmented need to flip
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = matrix[path[temp]][cur]
                        if entry[1] <= 0: # Already augmented need to flip
                            entry[1] -= total
                        else:
                            entry[0] += total
                        cur = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = top
                    queue.append(i)
    return False

def answer(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    aug = []
    for i in range(len(path)):
        aug.append([])
        for j in range(len(path[i])):
            aug[i].append([0, path[i][j]])
        aug[i].append([0, 0])
        if i in exits:
            aug[i].append([0, max_val])
        else:
            aug[i].append([0, 0])
    aug.append([])
    aug.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            aug[-2].append([0, max_val])
        else:
            aug[-2].append([0, 0])
        aug[-1].append([0, 0])
    while bfs(aug, len(aug)-2, len(aug)-1):
        pass
    total = 0
    for i in range(len(aug)):
        total += aug[-2][i][0]
    return total