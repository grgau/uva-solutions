from copy import deepcopy
import heapq

puzzle_lines = 4
puzzle_cols = 4

final_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def h_mann(state):
  global final_state
  distance = 0
  for i in range(puzzle_lines):
    for j in range(puzzle_cols):
      if state[i][j] == 0 or final_state[i][j] == 0:
        continue
      elif state[i][j] != final_state[i][j]:
        distance += abs(i - (state[i][j]/puzzle_lines)) + abs(j -  (state[i][j]%puzzle_cols))
  return distance

def swap_up(state, lin, col):
  state_puzzle = deepcopy(state)
  aux_value = state_puzzle[lin][col]
  state_puzzle[lin][col] = state_puzzle[lin-1][col]
  state_puzzle[lin-1][col] = aux_value
  return state_puzzle, "U"


def swap_down(state, lin, col):
  state_puzzle = deepcopy(state)
  aux_value = state_puzzle[lin][col]
  state_puzzle[lin][col] = state_puzzle[lin+1][col]
  state_puzzle[lin+1][col] = aux_value
  return state_puzzle, "D"

def swap_left(state, lin, col):
  state_puzzle = deepcopy(state)
  aux_value = state_puzzle[lin][col]
  state_puzzle[lin][col] = state_puzzle[lin][col-1]
  state_puzzle[lin][col-1] = aux_value
  return state_puzzle, "L"

def swap_right(state, lin, col):
  state_puzzle = deepcopy(state)
  aux_value = state_puzzle[lin][col]
  state_puzzle[lin][col] = state_puzzle[lin][col+1]
  state_puzzle[lin][col+1] = aux_value
  return state_puzzle, "R"


def expand_current(state):
  next_states = [] # Lista de novos estados gerados para cada movimentação possível
  state_puzzle = state[1] # Copia o puzzle da tupla (distancia_solução, puzzle)
  space_value = 0 # Valor que representa espaço vazio

  # Encontra posição do 9 e coloca nas variáveis lin e col
  space_pos = [(index, row.index(space_value)) for index, row in enumerate(state_puzzle) if space_value in row][0]
  lin = space_pos[0]
  col = space_pos[1]

  # Pode mover pra baixo e pra direita
  if(lin == 0 and col == 0):
    next_states.append(swap_down(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))

  # Pode mover pra baixo, pra direita e pra esquerda
  if((lin == 0 and col == 1) or (lin == 0 and col == 2)):
    next_states.append(swap_down(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin, col))

  # Pode mover pra esquerda e pra baixo
  if(lin == 0 and col == 3):
    next_states.append(swap_left(state_puzzle, lin, col))
    next_states.append(swap_down(state_puzzle, lin, col))
    
  # Pode mover pra cima, pra direita e pra baixo
  if(lin == 1 and col == 0):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))
    next_states.append(swap_down(state_puzzle, lin, col))

  # Pode mover pra cima, pra baixo, pra esquerda e pra direita
  if((lin == 1 and col == 1) or (lin == 1 and col == 2) or (lin == 2 and col == 1) or (lin == 2 and col == 2)):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_down(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))
    
  # Pode mover pra cima, pra esquerda e pra baixo
  if(lin == 1 and col == 3):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin, col))
    next_states.append(swap_down(state_puzzle, lin, col))

  # Pode mover pra cima, pra direita e pra baixo
  if(lin == 2 and col == 0):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))
    next_states.append(swap_down(state_puzzle, lin, col))

  # Pode mover pra cima, pra esquerda e pra baixo
  if(lin == 2 and col == 3):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin,col))
    next_states.append(swap_down(state_puzzle, lin, col))

  # Pode mover pra cima e pra direita
  if(lin == 3 and col == 0):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_right(state_puzzle, lin, col))

  # Pode mover pra cima, pra esquerda e pra direita
  if((lin == 3 and col == 1) or (lin == 3 and col == 2)):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin,col))
    next_states.append(swap_right(state_puzzle, lin, col))

  # Pode mover pra cima e pra esquerda
  if(lin == 3 and col == 3):
    next_states.append(swap_up(state_puzzle, lin, col))
    next_states.append(swap_left(state_puzzle, lin,col))

  return next_states

def A_star(initial_state):
  global final_state
  queue = []
  expanded = {}
  heapq.heappush(queue, (0, initial_state[0]))
  expanded[str(initial_state[0])] = ""

  while (len(queue) != 0):
    current_state = heapq.heappop(queue)
    nivel = len(expanded[str(current_state[1])])
    if current_state[1] == final_state:
      return expanded[str(current_state[1])]

    next_states = expand_current(current_state)
    for state in next_states: # Cada state é constituido por: (estado do tabuleiro, direção do movimento)
      if(str(state[0]) not in expanded.keys()):
        expanded[str(state[0])] = expanded[str(current_state[1])] + state[1]
        f = nivel + 1 + h_mann(state[0])
        heapq.heappush(queue, (f, state[0]))
  return "This puzzle is not solvable."

def is_solvable(puzzle):
  space_value = 0
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
  global final_state
  puzzle = []
  number_of_cases = int(input())
  for case in range(number_of_cases):
    for i in range(puzzle_lines):
        puzzle.append(list(map(int, input().split())))
    if is_solvable(puzzle):
      print(A_star((puzzle, "")))
    else:
      print("This puzzle is not solvable.")
    puzzle = []
main()
