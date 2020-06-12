entrances = []
sum_numbers = []
solutions = []

def sum_it_up(index, numbers_sum):
  global sum_numbers
  global solutions
  if t == numbers_sum:
    new_list = sum_numbers[:]
    if new_list not in solutions:
      print(*sum_numbers, sep="+")
      solutions.append(new_list)
      return

  for i in range(index, n):
    if int(entrances[i]) + numbers_sum <= t:

      numbers_sum += int(entrances[i])
      sum_numbers.append(int(entrances[i]))

      sum_it_up(i+1, numbers_sum)
      
      numbers_sum -= int(entrances[i])
      sum_numbers.pop(-1)

def main():
  global t
  global n
  global entrances
  global sum_numbers
  global solutions

  entrances = list((input().split()))
  while not entrances == ["0", "0"]:
    t = int(entrances[0])
    n = int(entrances[1])
    entrances.pop(0)
    entrances.pop(0)
    print("Sums of %d:" % t)
    sum_it_up(0, 0)
    
    if solutions == []:
      print("NONE")
    
    entrances = list((input().split()))
    solutions = []

main()