# Pedro Henrique Ferracini de Barros

sky = []
r = 0
c = 0

def check_if_valid(i, j):
  if (i >= 0 and j >= 0) and (i < r and j < c) and sky[i][j] == "*":
    return True # Retorna somente pontos válidos na matriz sky e que tem vizinho "*"
  return False

def count_stars(sky):
  stars = 0
  graph = {}
  for i in range(r):
    for j in range(c):
      if sky[i][j] == "*": # Se achar "*", checka os 8 vizinhos do ponto
        values = []
        if check_if_valid(i-1, j-1):
          values.append(sky[i-1][j-1])
        if check_if_valid(i-1, j):
          values.append(sky[i-1][j])
        if check_if_valid(i-1, j+1):
          values.append(sky[i-1][j+1])
        if check_if_valid(i, j-1):
          values.append(sky[i][j-1])
        if check_if_valid(i, j+1):
          values.append(sky[i][j+1])
        if check_if_valid(i+1, j-1):
          values.append(sky[i+1][j-1])
        if check_if_valid(i+1, j):
          values.append(sky[i+1][j])
        if check_if_valid(i+1, j+1):
          values.append(sky[i+1][j+1])

        graph[str((i,j))] = values # Os grafos que tiverem uma lista de pontos vazias são as estrelas

  # Os grafos serao por ex: {'(1, 4)': ['*'], '(2, 4)': ['*', '*'], '(3, 3)': ['*'], '(4, 0)': []}, grafos podem ser representados por dicionarios em python
  # Onde as chaves, por ex (1, 4) sao onde tem "*" na matriz de entrada e as listas quantas "*" vizinhas, logo uma estrela tem valor: []

  for key, value in graph.items():
    if value == []: # Conta quantos [], isto eh, caracteres "*" somente com "." como vizinhos
      stars += 1
  return stars

def main():
  global sky
  global r
  global c

  sky = []
  r, c = map(int, input().split(" "))
  while r != 0 and c != 0:
    for row in range(r):
      sky.append([char for char in input()]) # Constroi matriz que representa o ceu
    print(count_stars(sky))
    sky = []
    r, c = map(int, input().split(" "))

main()