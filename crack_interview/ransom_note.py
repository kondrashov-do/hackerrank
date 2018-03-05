from collections import defaultdict
def ransom_note(magazine, ransom):
    if len(magazine) < len(ransom):
        return False
    words_dict = defaultdict(int)
    for word in magazine:
        words_dict[word] += 1
    for word in ransom:
        if words_dict[word] == 0: return False
        words_dict[word] -= 1
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")