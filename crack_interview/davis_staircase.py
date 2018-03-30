def num_of_ways_to_top_with_mem(num_of_stairs, memo_list):
    if num_of_stairs <= 1:
        return 1
    if num_of_stairs == 2:
        return 2
    if num_of_stairs == 3:
        return 4
    else:
        if memo_list[num_of_stairs] == 0:
            memo_list[num_of_stairs] = num_of_ways_to_top_with_mem(num_of_stairs-1, memo_list) + num_of_ways_to_top_with_mem(num_of_stairs-2, memo_list) + num_of_ways_to_top_with_mem(num_of_stairs-3, memo_list)
    return memo_list[num_of_stairs]
    
    
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    memo_list = [0] * (n+1)
    #print(memo_list)
    print(num_of_ways_to_top_with_mem(n, memo_list))