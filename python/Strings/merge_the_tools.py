def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = set()
        for char in string[i:i+k]:
            if char not in s:
                print(char, end='')
                s.add(char)
        print()
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
