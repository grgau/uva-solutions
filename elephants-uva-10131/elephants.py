MAX_ELEPHANTS = 1000
MAX_W, MAX_IQ = 10000, 10000
elephants = []
dp = [1] * MAX_ELEPHANTS
sequence = [0] * MAX_ELEPHANTS

def print_sequence(lenght):
  print(elephants[lenght][0]) # Printa qual a posição do primeiro elefante da lista inicial
  if sequence[lenght]: # Se valor diferente de zero nessa sequencia
    print_sequence(sequence[lenght]) # Chama recursivo pra printar o resto da sequence
  else:
    print(elephants[0][0]) # Printa a posição do elefante na lista inicial do primeiro elefante

def longest_sequencePD():
  global dp
  global sequence
  for i in range(len(elephants)):
    for j in range(i):
      if elephants[j][2] < elephants[i][2] and dp[j] > dp[i] - 1: # Só vai "salvar" o elefante na sequencia para printar e no array dp que guarda os resultados da programação dinamica se:
        sequence[i] = j                                           # O QI do elefante da subsequencia for menor que o comparado da sequencia e o array dp que guarda os resultados na posição j foir maior que na posição[i] - 1, isto é, dp[j] adiciona em 1 elefante a otimização
        dp[i] = dp[j] + 1

  for i in range (len(elephants)):
    if dp[i] < dp[i + 1]:
      lenght = i + 1 # Variavel auxiliar pra contar quantos elefantes da sequencia mais longa

  print(dp[lenght]) # Printa quantidade de elefantes
  print_sequence(lenght) # Método pra printar recursivo a sequencia de elefantes

def main():
  global elephants
  weight, iq = map(int, input().split(" "))
  count = 0

  while(True):
    count += 1
    elephants.append((count, weight, iq)) # Cada elegante é uma tupla (posição_elefante_lista, peso, qi)
    try:
      weight, iq = map(int, input().split(" "))
    except EOFError:
      elephants.sort(key=lambda x: x[1] if x[1] != x[2] else x[2], reverse=True) # Ordena os elefantes por maior peso e depois por QI
      longest_sequencePD()
      break

main()