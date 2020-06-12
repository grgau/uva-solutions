campsite_distances = []
number_nights = 0

def check_path(path):
  distance = 0
  n = 0 # n conta o numero de noites para cada checagem, numero de noites max está em number_nights
  for campsite in campsite_distances:
    if path < campsite: # Tamanho de caminho (MID) insuficiente para chegar ao proximo acampamento
      return False
    else:
      if path >= distance + campsite: # Se tamanho de caminho (MID) passou do acampamento + distancia
        distance += campsite
      else:
        distance = campsite
        n += 1 # Conta uma noite a mais passada

  if path >= distance:
    n += 1

  return False if n-1 > number_nights else True # Retorna false se extrapolar numero de noites


def binary_search(low, high): # Divide o caminho as distancias em duas partes e busca
  while low < high:
    mid = (low+high)//2
    if check_path(mid):
      high = mid
    else:
      low = mid + 1
  return low if check_path(low) else high

def main():
  global campsite_distances
  global number_nights
  distances = 0
  while True:
    try:
      entrance = input()
      if entrance != "":
        number_campsites, number_nights = map(int, entrance.split())
        for campsite in range(number_campsites+1):
          campsite = int(input())
          campsite_distances.append(campsite)
          distances += campsite
        print(binary_search(0, distances))
        campsite_distances = []
        distances = 0
    except EOFError:
      break

main()