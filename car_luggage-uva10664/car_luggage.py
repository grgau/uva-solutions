MAX_WEIGHT_POSSIBLE = 200
MAX_SUITCASES = 20
cars_weight = ["NO"] * (MAX_WEIGHT_POSSIBLE + 1) # Marca todas as posições de pesos possiveis do carro para "NO", inicializando

def main():
  global suitcases
  global cars_weight
  number_of_cases = int(input())

  for case in range(number_of_cases):
    suitcases = list(map(int, input().split())) # Le pesos das malas de entrada

    sum_of_suitcase_weights = sum(suitcases)
    if sum_of_suitcase_weights % 2 == 0: # Pra dividir peso igualmente entre carros, precisa ter total de peso par
      for weight_suitcase in range(len(suitcases)): # Para cada peso da mala
        for weight_car in range(sum_of_suitcase_weights//2, suitcases[weight_suitcase], -1): # Para cada peso do carro, começando em metade do total do peso das malas até o peso da mala atual do laço
          cars_weight[weight_car] = "YES" # Marca como "YES" a posição do peso, isto é, pode distribuir o peso igual entre os carros para essa posição de peso

    print(cars_weight[sum_of_suitcase_weights//2]) # Se na posição da metade total dos pesos de cars_weight estiver com "YES" quer dizer que pode carregar igualmente entre os carros, senão vai ser "NO" 
main()