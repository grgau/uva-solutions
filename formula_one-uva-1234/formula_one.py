# Pedro Henrique Ferracini de Barros

max_v = 100
adj_list = [] # Define grafo como lista de adjacencia
rank = [0 for _ in range(max_v)] # Rank usado no union_find
parent = [0 for _ in range(max_v)] # Parent usado no union_find

def union_find(N):
  global rank
  global parent

  rank = [0 for _ in range(max_v)] # Zera rank
  for i in range(N): # Atribui parent pra si proprio
    parent[i] = i

def find(vertice):
  if parent[vertice] != vertice:
    parent[vertice] = find(parent[vertice])
  return parent[vertice]

def is_same_set(i, j):
  return find(i) == find(j)

def union(i, j): # Union semelhante ao visto na sala de aula
  global rank
  global parent

  if not is_same_set(i, j):
    x = find(i)
    y = find(j)

    if rank[x] > rank[y]:
      parent[y] = x
    else:
      parent[x] = y
      if rank[x] == rank[y]:
        rank[y] += 1

def kruskall_mst():
  global adj_list
  union_find(max_v) # Inicia union_find
  adj_list = sorted(adj_list, reverse=True) #Ordena ao contrario, pois queremos max tree
  cost = 0

  for i in range(len(adj_list)):
    arr = adj_list[i]
    if not is_same_set(arr[1][0], arr[1][1]): # Se nao for do mesmo conjunto, faz uniao
      union(arr[1][0], arr[1][1])
    else: # Se for do mesmo conjunto, soma no custo (custo de onde por a camera)
      cost += arr[0]

  return cost

def main():
  global adj_list

  number_datasets = int(input())
  while number_datasets != 0:
    n, m = map(int, input().split())

    for road in range(m):
      junction1, junction2, cost = map(int, input().split())
      adj_list.append((cost, (junction1, junction2))) # Grafo no formato [(cost, (verticeX, verticeY)), ...]

    print(kruskall_mst())
    adj_list = [] # Limpa grafo de adjacencia
    number_datasets -= 1
main()