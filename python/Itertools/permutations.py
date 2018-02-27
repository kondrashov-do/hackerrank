from itertools import permutations
input_list = input().split()
input_string = ''.join(sorted(input_list[0]))
for item in permutations(input_string, int(input_list[1])):
    print(''.join(item))