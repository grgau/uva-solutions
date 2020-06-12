# Pedro Henrique Ferracini de Barros

division_number = 131071

def main():
  line_input = input() # O metodo input nao le apos um "\n", entao foi preciso algumas mudancas
  raw_string = []

  while line_input:
    n = 0
    try:
      raw_string.extend(line_input) # Vai salvando cada input em um array de chars

      for i in range(len(raw_string)):
        if raw_string[i] == "#": # Se encontra um "#" considera que acabou o numero binario de varias linhas
          for ch in raw_string[0:i]:
            n = (n*2 + (int(ch))) % division_number # Transforma o binario em int e divide pelo division_number, pegando resto
          if n == 0:
            print("YES") # Se resto zero, retorna "YES"
          else:
            print("NO") # Se resto diferente de zero, retorna "NO"
          raw_string = []

      line_input = input()
    except EOFError:
      break

main()