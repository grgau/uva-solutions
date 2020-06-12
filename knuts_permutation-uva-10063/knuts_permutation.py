entrance = ""
answers = []
def knuts_permutation(permut_string, string_len):
  global entrance
  global answers
  if string_len == len(entrance):
    answers.append(permut_string)
    return
  for i in range(string_len+1):
    sub1 = permut_string[0:i]
    sub2 = permut_string[i:string_len]
    knuts_permutation(sub1+entrance[string_len]+sub2, string_len+1)

def main():
  global entrance
  global answers
  while True:
    try:
      entrance = input()
      knuts_permutation(entrance, 0)
      answers.append("")
    except EOFError:
      break
  print("\n".join(answers[0:len(answers)-1]))
main()