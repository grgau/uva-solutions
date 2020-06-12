# Pedro Henrique Ferracini de Barros

rows = 0
columns = 0
maze = []
commands = []
directions = ["N", "E", "S", "W"]

def move_robot(row, column):
  robot_face = 0 # 0 Representa o norte, virar sentido horario soma 1 e sentido anti-horario subtrai 1

  for command in commands:
    if command == "R":
      robot_face += 1
    elif command == "L":
      robot_face -= 1
    elif command == "Q":
      break
    elif command == "F":
      direction_to_move = directions[robot_face % 4] # Essa operação retorna uma das direções "N", "E", "S", "W" de acordo com valor robot_face, mesmo se negativa, em python a lista é lida ao contrario
      if direction_to_move == "N":
        if row-1 >= 0 and maze[row-1][column] == " ": # Verifica se pode mover (dentro do tabuleiro e não for parede)
          row -= 1
      elif direction_to_move == "E":
        if column+1 < columns and  maze[row][column+1] == " ": # Verifica se pode mover (dentro do tabuleiro e não for parede)
          column += 1
      elif direction_to_move == "S":
        if row+1 < rows and maze[row+1][column] == " ": # Verifica se pode mover (dentro do tabuleiro e não for parede)
          row += 1
      elif direction_to_move == "W":
        if column-1 >= 0 and maze[row][column-1] == " ": # Verifica se pode mover (dentro do tabuleiro e não for parede)
          column -= 1

  return("{0} {1} {2}".format(row+1, column+1, directions[robot_face % 4]))

def main():
  global maze
  global commands
  global rows
  global columns

  number_of_cases = int(input())
  _ = input() # Le linha em branco
  while True:
    try:
      rows, columns = map(int, input().split())
      for row in range(rows):
        maze.append([char for char in input() if char != "\r"]) # Cada caractere é um indice da matriz
      initial_row, initial_column =  map(int, input().split()) # Le posição inicial
      commands = [char for char in input()] # Lê lista de comandos, cada comando um elemento do vetor
      print(move_robot(initial_row-1, initial_column-1)) # Indice da coluna e linha passado no problema começa em 1,1 e armazenada em 0,0
      
      if number_of_cases != 1: print("") # Serve de controle para printar as linhas em branco
      number_of_cases -= 1
      
      _ = input() # Le linha em branco
      maze = [] # Zera labirinto
      commands = [] # Zera comandos
    except EOFError:
      break
main()