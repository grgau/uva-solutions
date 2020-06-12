# Pedro Henrique Ferracini de Barros

from collections import defaultdict

INF = 9999
max_n = 10
adj_list = defaultdict(list) # Define grafo como lista de adjacencia

def check_negative_cycles(distance): # Checagem de ciclo negativo semelhante a vista em aula
  for u in range(max_n):
    for j in range(len(adj_list[u])):
      v = adj_list[u][j]
      if distance[u] + v[1] < distance[v[0]]:
        print("possible")
        return

  print("not possible")
  return

def bellman_ford(s): # Algoritmo bellman_ford semelhante ao visto em aula
  distance = [INF for _ in range(max_n)] # Vetor de distancias
  distance[s] = 0

  for i in range(max_n-1):
    for u in range(max_n):
      for j in range(len(adj_list[u])):
        v = adj_list[u][j]

        if distance[u] + v[1] < distance[v[0]]:
          distance[v[0]] = distance[u] + v[1]

  return distance

def main():
  global adj_list

  number_cases = int(input())
  for case in range(number_cases):
    n, m = map(int, input().split())

    for star_system in range(m):
      x, y, t = map(int, input().split())
      adj_list[x].append((y, t))

    distance = bellman_ford(0)
    check_negative_cycles(distance)
    adj_list = defaultdict(list) # Zera lista de adjacencias para proximo caso
main()