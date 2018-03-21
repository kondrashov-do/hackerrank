word_dict = {}
word_arr = []
for i in range(int(input())):
    word = input()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_arr.append(word)
        word_dict[word] = 1
print(len(word_dict))
for item in word_arr:
    print(str(word_dict[item]), end=' ')