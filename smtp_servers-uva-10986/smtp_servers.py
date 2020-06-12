# Pedro Henrique Ferracini de Barros

from collections import defaultdict
import heapq

max_servers = 20
INF = 99999
adj_list = defaultdict(list) # Define grafo como lista de adjacencia

def dijkstra(S, T):
  pq = [] # Lista de prioridade
  distance = [INF for i in range(max_servers)] # Vetor de distancias

  distance[S] = 0
  heapq.heappush(pq, (0, S))

  while pq: # Implementacao de DJIKSTRA semelhante a vista em aula
    pu = heapq.heappop(pq)
    du = pu[0]
    u = pu[1]

    if du > distance[u]: # Se distancia do noh retirado da fila maior, desconsidera
      continue

    # Se distancia armazenada do noh v eh maior que distancia armazenada do u + peso do v, salva nova distancia
    for j in range(len(adj_list[u])):
      v = adj_list[u][j]
      if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        heapq.heappush(pq, (distance[v[0]], v[0]))

  return distance[T] if distance[T] != INF else "unreachable" # Retorna a distancia de T, se for INF, retorna unreachable

def main():
  global adj_list
  number_cases = int(input())

  for case in range(number_cases):
    blank_line = input() # Previne leitura de linhas em branco no input
    n, m, S, T = map(int, input().split())
    for server in range(m):
      i, j, w = map(int, input().split())
      adj_list[i].append((j, w))
      adj_list[j].append((i, w)) # Adiciona lista de adjacencias a bidirecao do grafo

    print("Case #%d: %s" % (case+1, dijkstra(S, T)))
    adj_list = defaultdict(list) # Zera lista de adjacencias para proximo caso
main()