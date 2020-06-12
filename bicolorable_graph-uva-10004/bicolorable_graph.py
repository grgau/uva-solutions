# Pedro Henrique Ferracini de Barros

def can_colorate(adj_matrix, color, pos, c, n):
  if color[pos] != -1 and color[pos] != c: # Nao pode mais pintar pois cor ja foi mudada de -1 para c, e c nao eh a mesma que pretende-se colorir agora
    return False 

  color[pos] = c # Marca em array color, a cor c
  ans = True 
  for i in range(0, n):
    if adj_matrix[pos][i]:
      if color[i] == -1:
        ans = can_colorate(adj_matrix, color, i, 1-c, n) # Usa DFS para tentar colorir os nos adjacentes

      if color[i] != -1 and color[i] == c: # Nao pode colorir, noh ja foi colorido e cor que quer colorir eh a mesma do noh anterior
        return False

    if not ans:
      return False

  return True

def main():
  n = int(input())
  l = int(input())
  adj_matrix = [[0] * n for _ in range(n)] # Matriz de adjacencia do grafo (n x n)
  color = [-1] * n # Cores

  while True:
    try:
      for edge in range(l):
        nodes = list(map(int,input().split()))
        adj_matrix[nodes[0]][nodes[1]] = 1 # Preenchimento da matriz de adjacencia

      if can_colorate(adj_matrix, color, 0, 0, n): print("BICOLORABLE.")
      else: print("NOT BICOLORABLE.")

      n = int(input())
      l = int(input())
      adj_matrix = [[0] * n for _ in range(n)]
      color = [-1] * n
    except EOFError:
      break

main()