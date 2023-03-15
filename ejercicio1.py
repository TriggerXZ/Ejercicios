arr = [1, 6, 9, 3, 5]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == 10:
            print(arr[i], arr[j])
