def merge(left_half, right_half):
    inv = 0
    i=0
    j=0
    arr_left_len = len(left_half)
    arr_right_len = len(right_half)
    res_arr = []
    while i < arr_left_len and j < arr_right_len:
        if left_half[i] <= right_half[j]:
            res_arr.append(left_half[i])
            i += 1                
        else:
            res_arr.append(right_half[j])
            j=j+1
            inv += arr_left_len - i
    if i < arr_left_len:
        res_arr += left_half[i:]
    elif j < arr_right_len:
        res_arr += right_half[j:]
    return res_arr, inv
        
def sort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        arr1, inv1 = sort(left_half)
        arr2, inv2 = sort(right_half)
        res_arr, inv = merge(arr1, arr2)
        return res_arr, inv+inv1+inv2
    else:
        return arr, 0
      
def count_inversions(arr):
    _, result = sort(arr)
    return result
      

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))