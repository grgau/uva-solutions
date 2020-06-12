from copy import deepcopy

puzzle_lines = 3
puzzle_cols = 3

final_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def swap_right(state, line): # Copia o estado atual e devolve novo estado com elementos da linha "line" movidos para direita
  next_state = deepcopy(state)
  aux = next_state[line][2]
  next_state[line][2] = next_state[line][1]
  next_state[line][1] = next_state[line][0]
  next_state[line][0] = aux
  return next_state

def swap_up(state, column): # Copia o estado atual e devolve novo estado com elementos da coluna "column" movidos para cima
  next_state = deepcopy(state)
  aux = next_state[0][column]
  next_state[0][column] = next_state[1][column]
  next_state[1][column] = next_state[2][column]
  next_state[2][column] = aux
  return next_state

def bfs(initial_state):
  global final_state
  queue = []
  moves = {}
  queue.append(initial_state)
  moves[str(initial_state)] = ""

  while (len(queue) != 0):
    current_state = queue.pop(0)
    if current_state == final_state: # Se current retirado da frente da fila for resposta, retorna quantidade de movimentos e quais
      return str(len(moves[str(current_state)])//2) + " " + str(moves[str(current_state)])

    for i in range(puzzle_lines): # Para cada uma das linhas, move para direita elementos
      aux = swap_right(current_state, i)
      if(str(aux) not in moves.keys()): # Se não esta em dicionario novo estado, acrescenta
        moves[str(aux)] = moves[str(current_state)] + "H" + str(i+1) # Salva os movimentos com direção e linha
        queue.append(aux) # Coloca no fim da fila de estados

    for j in range(puzzle_cols): # Para cada uma das colunas, move para cima elementos
      aux = swap_up(current_state, j)
      if(str(aux) not in moves): # Se não esta em dicionario novo estado, acrescenta
        moves[str(aux)] = moves[str(current_state)] + "V" + str(j+1) # Salva os movimentos com a direção e coluna
        queue.append(aux) # Coloca no fim da fila de estados
  return "Not solvable"

def is_solvable(puzzle):
  space_value = 9
  flat_puzzle = [item for sublist in puzzle for item in sublist]
  space_pos = [(index, row.index(space_value)) for index, row in enumerate(puzzle) if space_value in row][0]
  lin = abs(space_pos[0] - puzzle_lines)
  inversions = 0

  for i in range(puzzle_lines * puzzle_cols):
    for j in range(i + 1, puzzle_lines * puzzle_cols):
      if flat_puzzle[j] and flat_puzzle[i] and flat_puzzle[i] > flat_puzzle[j]:
        inversions += 1

  if puzzle_lines % 2: # Tabuleiro impar
    return not inversions % 2 # Numero de inversões par
  else: # Tabuleiro par
    if lin % 2: # Linha impar
      return not inversions % 2 # Numero de inverões par
    else: # Linar par
      return inversions % 2 # Numero de inversões ímpar

def main():
  global puzzle_cols
  puzzle = []

  while True:
    try:
      for i in range(puzzle_cols):
        entrance = input()
        if entrance == "0":
          return
        else:
          puzzle.append(list(map(int, entrance.split())))
      if is_solvable(puzzle):
        print(bfs(puzzle))
      else:
        print("Not solvable")
      puzzle = []
    except EOFError:
      return

main()
