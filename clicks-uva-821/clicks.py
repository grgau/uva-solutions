# Pedro Henrique Ferracini de Barros

def main():
  INF = 10
  max_nodes = 101
  case = 0

  input_nodes = [int(x) for x in input().split()]

  while input_nodes != [0, 0]:
    case += 1
    node_counter = 0
    sum_of_dists = 0
    graph = [[INF] * max_nodes for _ in range(max_nodes)] # Cria matriz de adjacencia de tamanho de max_nodes, com valores infinitos

    for i in range(0, len(input_nodes), 2):
      if input_nodes[i] != 0:
        graph[input_nodes[i]][input_nodes[i+1]] = 1 # Cria grafo

    for node in graph:
      if 1 in node:
        node_counter += 1 # Conta quantos nos tem no grafo, checando se cada linha da matriz possui 1

    for i in range(max_nodes):
      for j in range(max_nodes):
        if i == j:
          graph[i][j] = 0 # Atribui 0 para diagonal

    input_nodes = list(set(input_nodes)) # Remove valores duplicados para velocidade em comparacao

    # Floyd Warshall
    for k in range(max_nodes):
      if k in input_nodes:
        for i in range(max_nodes):
          if i in input_nodes:
            for j in range(max_nodes):
              if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(max_nodes):
      for j in range(max_nodes):
        if graph[i][j] != 0 and graph[i][j] != INF:
          sum_of_dists += graph[i][j] # Conta soma das distancias que nao sao 0 ou infinito

    print("Case %d: average length between pages = %.3f clicks" % (case, sum_of_dists/(node_counter * (node_counter-1))))

    input_nodes = [int(x) for x in input().split()]
main()