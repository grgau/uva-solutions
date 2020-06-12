# Pedro Henrique Ferracini de Barros

sieve_size = 100
sieve = [1 for _ in range(sieve_size * sieve_size)]
primes = []

def create_sieve(max_value): # Cria o Crivo de Eratostenes conforme visto em aula
  global sieve
  global primes
  sieve[0] = 0
  sieve[1] = 1
  sieve_size = max_value + 1

  for i in range (2, sieve_size + 1):
    if sieve[i]:
      for j in range(i*i, sieve_size + 1, i):
        sieve[j] = 0
      primes.append(i)

def calculate_primes(N): # Fatoracao em numeros primos
  factors = [0 for _ in range(N+1)]
  for i in range(len(primes)):
    p = primes[i]
    while N//p > 0: # Enquanto numero de entrada dividido pelos primos calculados no crivo maior que zero (encontra os primos menores)
      factors[primes[i]] += N//p # Salva como um valor possivel de fatoracao
      p *= primes[i]

  return factors

def main ():
  create_sieve(100) # Cria crivo ate 100

  number = int(input())
  while number != 0:
    print(str(number) + "! =", end=" ")
    for value in calculate_primes(number):
      if value != 0:
        print(value, end=" ")
    print("")
    number = int(input())

main()