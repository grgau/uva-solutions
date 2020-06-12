input_matrix = int(input())

for  each_case in range(input_matrix):
  n = int(input())
  fields = list(input())
  maxScarecrows = 0

  for j in range(len(fields)):
    if fields[j] == ".":
      maxScarecrows += 1
      if j+1 < len(fields):
        fields[j+1] = "#"
      if j+2 < len(fields):
        fields[j+2] = "#"

  print("Case " + str(each_case+1) + ": " + str(maxScarecrows))