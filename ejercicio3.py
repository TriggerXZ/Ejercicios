arr = [1, 2, 1, 3, 3, 1, 2, 1, 5, 1]

dic = {}

for i in range(1, 6):
    dic[i] = arr.count(i)

for a, f in sorted(dic.items()):
    print(str(a) + ': '+'*'*f)
