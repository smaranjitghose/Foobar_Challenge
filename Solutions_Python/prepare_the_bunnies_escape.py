def shortest_path(sx, sy, maze):
    w = len(maze[0])
    h = len(maze)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if maze[nx][ny] == 1:
                  continue
                arr.append((nx, ny))

    return board


def solution(maze):
  w = len(maze[0])
  h = len(maze)
  tb = shortest_path(0, 0, maze)
  bt = shortest_path(h-1, w-1, maze)
  board = []

  ans = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          if tb[i][j] and bt[i][j]:
              ans = min(tb[i][j] + bt[i][j] - 1, ans)
  return ans