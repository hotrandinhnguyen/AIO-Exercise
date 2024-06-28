def count_word_in_file(file):
    count_word = {}
    with open(file, 'r') as f:
        for line in f:
            list_word = line.split()
            for word in list_word:
                word = word.lower()
                if word in count_word:
                    count_word[word] += 1
                else:   
                    count_word[word] = 1
        return(count_word)

if __name__ == "__main__":
    file = "MODULE1/week2/P1_data.txt"
    print(count_word_in_file(file))
    

