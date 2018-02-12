def capitalize(s):
    for word in s[:].split():
        s = s.replace(word, word.capitalize())
    return s
if __name__ == '__main__':
    string = input()
    print(capitalize(string))
