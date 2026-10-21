arr = [1, -1, 0, 2, -4, 100, -100]

# bubble sort algorithm
# swap consecutive elements n-1 times 
# for each loop highest element is placed at its correct position

count = 1
n = len(arr)
while count <= n-1:
    i = 0
    while i <= n-1-count:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1
    count += 1
    
print(arr)

'''
# Optimized for already sorted list
arr = [1, -1, 0, 2, -4, 100, -100]

# bubble sort algorithm
# swap consecutive elements n-1 times 
# for each loop highest element is placed at its correct position

count = 1
n = len(arr)
while count <= n-1:
    i = 0
    swapped = False
    while i <= n-1-count:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
        i += 1
    count += 1
    if not swapped:
        break
    
print(arr)


'''
