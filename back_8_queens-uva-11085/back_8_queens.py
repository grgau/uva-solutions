entrance = []
positions = [None] * 8

def valid_position(row, col):
  for i in range(row):
    if col == positions[i]:
      return False
    if abs(row - i) == abs(col - positions[i]): #Se tiver mesma distancia estão na mesma diagonal
      return False
  return True

def eight_queens(row):
  global positions
  max_moves = 10000
  if row == len(entrance):
    return 0
  for col in range(len(entrance)):
    if valid_position(row, col):
      positions[row] = col
      if col == entrance[row]:
        max_aux = eight_queens(row + 1)
      else:
        max_aux = 1 + eight_queens(row + 1)
      max_moves = min(max_aux, max_moves)
  return max_moves

def main():
  global entrance
  global positions
  case = 1
  while True:
    try:
      entrance = [int(i) - 1 for i in input().split()]
      max_moves = eight_queens(0)
      print("Case {}: {}".format(case, max_moves))
      positions = [None] * 8
      case += 1
    except EOFError:
      break

main()