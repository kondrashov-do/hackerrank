n = int(input())
stack = []
for i in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
        if len(stack) == 1:
            max_elem = stack[0]
        max_elem = max(max_elem, query[1])
    elif query[0] == 2:
        if stack.pop() == max_elem and stack != []:
            max_elem = max(stack)
    elif query[0] == 3:
        print(max_elem)