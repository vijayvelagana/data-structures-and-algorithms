arr = [1, -1, 0, 2, -4, 100, -100, 0, -150, -200]

# Selection Sort, find the smallest element and swap it with the front 

n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
        
