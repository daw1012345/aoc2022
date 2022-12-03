import string
with open('day3/input.txt', 'r') as f:
    a = f.readlines()
    print(sum(list(map(lambda x: sum(map(lambda a: 1+string.ascii_letters.index(a), x)),map(lambda x: set(x[:len(x)//2]).intersection(set(x[len(x)//2:])), a)))))
    print(sum(list(map(lambda x: sum(map(lambda a: 1+string.ascii_letters.index(a), x)), [set(a[i].strip()).intersection(set(a[i+1].strip()), set(a[i+2].strip())) for i in range(0, len(a), 3)]))))