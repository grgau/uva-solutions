input_matrix = int(input())

for  each_case in range(input_matrix):
  n = int(input())
  maxCoins = 0
  previousCoin = 0
  totalCoins = 0

  coins = list((input().split()))

  for coin in coins:
    if (totalCoins + previousCoin) < int(coin):
      maxCoins += 1
      totalCoins += previousCoin  
    previousCoin = int(coin)

  print(maxCoins)