n, l_num= int(input()), input().split(" ")
l_num = [int(num) for num  in l_num]

while len(l_num) != 0:
    if n != len(l_num):
        n += len(l_num)
    minimum  = min(l_num)
    inds = [l_num.index(i) for i in l_num if i == minimum]
    value = iter(inds)
    while True:
        try:
            ind = next(value)
            l_num.pop(ind)
        except StopIteration:
            break
print(n)