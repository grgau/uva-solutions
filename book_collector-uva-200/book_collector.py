# Pedro Henrique Ferracini de Barros

def collating_sequence(list_of_strings):
  graph = {}
  sequence = []
  for string in list_of_strings: # Cria um grafo, cada noh eh a inicial da sequencia, os valores sao as sequencias que comecam com a letra, ex: {'X': ['XZY', 'XGY', 'XWY'], 'Z': ['ZXY', 'ZGW', 'ZGYZ'], 'Y': ['YWWX']}
    if string[0] in graph:
      graph[string[0]].append(string)
    else:
      graph[string[0]] = [string]

  for key, string_list in graph.items():
    if key not in sequence: # Coloca o noh do grafo se nao estiver ja nas sequencias, X... Y... Z
      sequence.append(key)
    
    for i in range(len(string_list)): # Para cada nos de uma letra inicial X, Y, Z por exemplo (['XZY', 'XGY', 'XWY'], ['ZXY', 'ZGW', 'ZGYZ'], ['YWWX'])
      for j in range(len(string_list[i])-1): # Para cada lista de um noh, por ex ['XZY', 'XGY', 'XWY']
        if i+1 < len(string_list): # Se nao for ultimo elemento da lista, por ex 'XWY'
          if len(string_list[i]) == len(string_list[i+1]): # Se essa lista e a proxima tem mesmo tamanho, por ex 'XZY', 'XGY'
            if string_list[i][j+1] == string_list[i+1][j+1]: # Se para cada letra, compara as seguintes, ex XZY e XGY, X = X, entao pega Z, pois entradas sao ordenadas
              if string_list[i][j] not in sequence: # Se ja nao estiver na sequencia, coloca
                sequence.append(string_list[i][j])

          if len(string_list[i]) != len(string_list[i+1]): # Se tamanhos diferentes, adiciona cada um dos caracteres que sobram de tamanho, por ex CA e CAE, adiciona E
            for k in range(len(string_list[i+1]) - len(string_list[i]), len(string_list[i+1])):
              if string_list[i+1][k] not in sequence: # Se caractere a ser adicionado nao estiver na sequencia ja
                sequence.append(string_list[i+1][k])
        elif len(string_list) != 1: # Se tamanho nao for 1, o que nao daria pra comparar, por ex 'X': ['XWY'], essa condicao serve pra pegar o ultimo elemento, por ex em 'Z': ['ZX', 'ZXY', 'ZXW'], pegaria 'ZXW'
          if string_list[i][j+1] not in sequence: # Se ultimo elemento nao esta na sequencia, adiciona
            sequence.append(string_list[i][j+1])
  return sequence


  print(graph)

def main():
  list_of_strings = []
  line = input()

  while True:
    try:
      if line != "#":
        list_of_strings.append(line)
      if line == "#":
        print(''.join(collating_sequence(list_of_strings)))
        list_of_strings = []
      line = input()
    except EOFError:
      break

main()