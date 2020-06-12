def main():
  entrance = input().split(" ")
  while len(entrance) == 4 and (entrance[0] != "0" or entrance[3] != "0"): # len(entrance) == 4 para casos "0 Fuel consumption 20" por exemplo, entrance[0] != "0" or entrance[3] != "0" para casos "0 Fuel consumption 0"
    begin = int(entrance[0]) # Primeiro valor da string "0 Fuel consumption..."
    consumption = int(entrance[3]) # Valor de consumption, por ex "0 Fuel consumption 5" pega o 5
    end, leak = 0, 0
    result, wasted_tank = 0.0, 0.0

    while(True):
      try:
        entrance = input().split(" ")
        end = int(entrance[0]) # Pega as posições 0 das entradas, por ex "10 Leak" pega o 10, "100 Goal" pega o 100
        # Calcula tanque
        wasted_tank += (end - begin) * consumption / 100.0
        wasted_tank += (end - begin) * leak

        if wasted_tank > result: # Atualiza pro maior valor entre resultado atual e o gasto do tank, pega o max
          result = wasted_tank

        if entrance[1] == "Goal": # Acabou o trajeto
          break
        elif entrance[1] == "Leak": # Aumenta o contador de leaks no gasto do tanque
          leak += 1
        elif entrance[1] == "Mechanic": # Zera as leaks no tanque
          leak = 0
        elif entrance[1] == "Gas" and entrance[2] == "station": # Abastece o gasto do tanque
          wasted_tank = 0.0
        else: # Mudou o valor do comsuption, tipo de entrada "100 Fuel consumption 30" por ex, pega o 30
          consumption = int(entrance[3])
        begin = end
      except EOFError:
        break
    print("%.3f" % round(result, 3))
    entrance = input().split(" ")

main()