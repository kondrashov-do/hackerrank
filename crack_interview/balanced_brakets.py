    def is_matched(expression):
        stack = []
        for chr in expression:
            if chr == '{': 
                stack.append('}')
            elif chr == '(':
                stack.append(')')
            elif chr == '[':
                stack.append(']')
            else:
                if stack == [] or stack.pop() != chr:
                    return False
        return stack == []

    t = int(input().strip())
    for a0 in range(t):
        expression = input().strip()
        if is_matched(expression) == True:
            print("YES")
        else:
            print("NO")
