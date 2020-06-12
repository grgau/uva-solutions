MAX_WEIGHT_POSSIBLE = 30

def maximizePD(max_goods, weight, W, P):
  # Cada posição de max_goods corresponde a um peso (max até 30), e cada posição guarda um preço
  return max(max_goods[weight], P + max_goods[weight - W]) # Pega max de valor atual de max_goods, ou max_goods do preço + posição de max_goods weight - W, as posições weight - W servem pra atualizar os valores ótimos pra cada posição do peso

def main():
  max_goods = [0]*(MAX_WEIGHT_POSSIBLE + 1) # Inicia lista de max_goods (valores que vão ser otimizados)

  # Leitura de quantidade de testes T, número de objetos N, preço e peso dos objetos P e W
  T = int(input())
  for case in range(T):
    N = int(input())
    for n_object in range(N):
      P, W = map(int, input().split())

      for weight in range(MAX_WEIGHT_POSSIBLE, -1, -1): # Peso máximo descrito no problema é 30, então faz for ao contrário
        if W <= weight:
          max_goods[weight] = maximizePD(max_goods, weight, W, P) # Chama função pra achar max e atualiza lista max_goods usada para prog dinamica

    result = 0
    G = int(input()) # Le G, numero de pessoas no grupo
    for people_in_group in range(G):
      result += max_goods[int(input())] # Cada índice de max_goods é um peso que pode ser carregado, e cada valor dessa posição é o resultado ótimo do preço pra aquele peso
    print(result)

main()