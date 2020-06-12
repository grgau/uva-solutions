import bisect

entrances = list((input().split()))
counter = 1

while not entrances == ["0", "0"]:
  bachelors = []
  spinsters = []
  n_bachelors = int(entrances[0])
  n_spinsters = int(entrances[1])

  for bachelor in range(1, n_bachelors+1):
    bisect.insort(bachelors, int(input()))

  for spinster in range(1, n_spinsters+1):
    bisect.insort(spinsters, int(input()))

  bachelors.reverse()
  spinsters.reverse()

  if len(bachelors) > len(spinsters):
    print("Case " + str(counter) + ": " + str(max(0, len(bachelors) - len(spinsters))), min(bachelors))
  else:
    print("Case " + str(counter) + ": " + str(max(0, len(bachelors) - len(spinsters))))

  counter += 1
  entrances = list((input().split()))