def split_array(array):
  middle = len(array)//2
  return array[:middle], array[middle:]

def combine(array1, array2):
  combined_array = []
  i, j, n = 0, 0, 0

  while i < len(array1) and j < len(array2):
    if array1[i] > array2[j]:
      combined_array.append(array2[j])
      n +=  (len(array2) - i)
      j += 1
    else:
      combined_array.append(array1[i])
      i += 1
  combined_array = combined_array + array1[i:] + array2[j:]
  return n, combined_array

def count_inversions(array):
  if len(array) == 1:
    return 0, array
  else:
    array1, array2 = split_array(array)
    n1, array1 = count_inversions(array1)
    n2, array2 = count_inversions(array2)
    n3, array = combine(array1, array2)
  return n1 + n2 + n3, array

def main():
  number_of_cases = int(input())
  for case in range(number_of_cases):
    array_size = int(input())
    array = list(map(int,input().split()))
    results, array = count_inversions(array)
    print(results)

main()