MAX_CHANGE = 30000 # Maximo de troco definido no problema
coins = [1, 5, 10, 25, 50] # Moedas possiveis para troco
coins_changes = [0] * (MAX_CHANGE + 1) # Array de possibilitades de trocos, usada na PD

def coinPD(change):
  global coins_changes

  if coins_changes[change] != 0: # Retorna valor que ja foi calculado para PD
    return coins_changes[change]

  for i in range(len(coins)):
    for j in range(coins[i], MAX_CHANGE):
      coins_changes[j] += coins_changes[j - coins[i]] # A partir do valor de moeda 1, 5, 10... acumula quantidade em cada posição j - coins[i]

  return coins_changes[change] # A posição change de coins_changes acumulou a quantidade de modos possiveis para valor troco change

def main():
  global coins_changes
  coins_changes[0] = 1

  change = int(input())
  
  while(True):
    result = coinPD(change)
    if result != 1:
      print("There are %d ways to produce %d cents change." % (result, change))
    else:
      print("There is only 1 way to produce %d cents change." % (change))
    try:
      change = int(input())
    except EOFError:
      break

main()