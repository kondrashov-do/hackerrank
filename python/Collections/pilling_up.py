for i in range(int(input())):
    size = int(input())
    horizontal_list = list(map(int, input().split()))
    #print(horizontal_list)
    vertical_list = []
    if horizontal_list[0] > horizontal_list[-1]:
        vertical_list.append(horizontal_list.pop(0))
    else:
        vertical_list.append(horizontal_list.pop())
    for i in range(1, size):
        if horizontal_list[-1] <= horizontal_list[0] and horizontal_list[0] <= vertical_list[i-1]:
            vertical_list.append(horizontal_list.pop(0))
        elif horizontal_list[0] <= horizontal_list[-1] and horizontal_list[-1] <= vertical_list[i-1]:
            vertical_list.append(horizontal_list.pop())
        else:
            print('No')
            #print(vertical_list)
            break
    if len(vertical_list) == size:
        print('Yes')