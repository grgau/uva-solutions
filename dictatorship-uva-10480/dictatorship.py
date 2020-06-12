# Pedro Henrique Ferracini de Barros

from copy import deepcopy

INF = 99999
max_v = 10
adj_matrix = [[0] * max_v for _ in range(max_v)]

def dfs(graph, s, visited):
  visited[s] = True
  for i in range(max_v):
    if graph[s][i] != 0 and not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, s, t, parent): # BFS
  visited = [0 for _ in range(max_v)]
  queue = []

  queue.append(s)
  visited[s] = True
  parent[s] = -1

  while len(queue) != 0:
    u = queue.pop(0)

    for v in range(max_v):
      if visited[v] == False and graph[u][v] > 0:
        queue.append(v)
        parent[v] = u
        visited[v] = True

  return visited[t] == True

def ford_fulkerson(s, t): # Implementa ford-fulkerson semelhante ao da aula
  residual = deepcopy(adj_matrix)
  cities_to_cut = []
  parent = [[None] * max_v for _ in range(max_v)]
  max_flow = 0

  while bfs(residual, s, t, parent):
    residual_min = INF

    v = t
    while(v != s):
      u = parent[v]
      residual_min = min(residual_min, residual[u][v])
      v = parent[v]

    v = t
    while(v != s):
      u = parent[v]
      residual[u][v] = residual[u][v] - residual_min
      residual[v][u] = residual[v][u] + residual_min
      v = parent[v]

    max_flow += residual_min

  visited = [False for _ in range(max_v)]
  dfs(residual, s, visited) # DFS serve para construir os nohs visitados no grafo residual

  for i in range(max_v): # Encontra valores diferentes de zero no grafo original e visitados
    for j in range(max_v):
      if visited[i] and (not visited[j]) and adj_matrix[i][j]:
        print("%d %d" % (i, j))
  print("")

def main():
  global adj_matrix
  cities, connections = map(int, input().split())

  while cities != 0 and connections != 0:
    for connection in range(connections):
      city1, city2, cost = map(int, input().split())
      adj_matrix[city1][city2] = cost # Preenchendo matriz de adjacencia bidirecional
      adj_matrix[city2][city1] = cost

    ford_fulkerson(1, 2)
    adj_matrix = [[0] * max_v for _ in range(max_v)] # Zera matriz de adjacencias para proximo caso
    new_input = input()
    cities, connections = map(int, input().split())
main()