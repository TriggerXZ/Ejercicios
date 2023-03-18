n1 = 0
n2 = 1
n3 = 0
for i in range(10):
    n1 = n2
    n2 = n3
    n3 = n1+n2
    print(n2)
