maze_size = 0
maze = []
possible_paths = []
path = []

def valid_position(x,y):
  try:
    maze[x][y]
  except IndexError:
    return False
  if maze[x][y] == "-" or maze[x][y] == "0":
    return False
  else:
    return True

def rat_maze(x, y):
  global maze
  global path
  global maze_size
  global possible_paths

  if valid_position(x,y) == False:
    return

  if x == maze_size-1 and y == maze_size-1:
    aux_list = path[:]
    possible_paths.append(aux_list);
    return

  maze[x][y] = "-"
  if valid_position(x, y+1):
    path.append("R")
    rat_maze(x, y+1)
    path.pop(-1)

  if valid_position(x+1, y):
    path.append("D")
    rat_maze(x+1, y)
    path.pop(-1)

  if valid_position(x, y-1):
    path.append("L")
    rat_maze(x, y-1)
    path.pop(-1)

  if valid_position(x-1, y):
    path.append("U")
    rat_maze(x-1, y)
    path.pop(-1)

  maze[x][y] = "1"

def main():
  global maze
  global path
  global maze_size
  global possible_paths

  new_possible_paths = []

  input_maze = int(input())

  for each_case in range(input_maze):
    maze_size = int(input())
    string_maze = list((input().split()))

    # Cria labirinto
    for i in range(0, len(string_maze), 4):
      maze.append(string_maze[i:i+4])

    path = []
    rat_maze(0, 0)

    # Formatando saida
    for path in possible_paths:
      new_path = ""
      for letter in path:
        new_path += letter
      new_possible_paths.append(new_path)

    new_possible_paths = sorted(new_possible_paths)
    print(*new_possible_paths, sep=" ")

    possible_paths = []
    new_possible_paths = []
    maze = []

main()
