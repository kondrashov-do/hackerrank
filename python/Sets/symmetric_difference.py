if __name__ == '__main__':
    m = int(input())
    m_set = set(map(int, input().split()))
    n = input()
    n_set = set(map(int, input().split()))
    sym_dif_list = list(m_set.difference(n_set))
    sym_dif_list.extend(list(n_set.difference(m_set)))
    #sym_dif_list.sort()
    for num in sorted(sym_dif_list):
        print(num)