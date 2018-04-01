def bubble_sort(arr):
    swap_num = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                swap_num += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('Array is sorted in %d swaps.' % swap_num)
    print('First Element: %d' % arr[0])
    print('Last Element: %d' % arr[-1])

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
bubble_sort(a)