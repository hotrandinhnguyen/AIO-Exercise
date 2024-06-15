def count_words_in_string(string : str):
  dic = {}
  for i in string:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  return dic

if __name__ == "__main__":
    string = "Happiness"
    print(count_words_in_string(string))
    string ="smiles"
    print(count_words_in_string(string))