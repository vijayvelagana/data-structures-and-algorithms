# Right Rotate and Left Rotate an array by k places

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    # time = O(n/2) = O(n)
    # space = O(1)
        
def right_rotate(arr, k):
    # Right rotate by k places
    # Reverse entire arr
    # Reverse first k 
    # Reverse remaining n-k
    
    print(f"Original arr: {arr}")
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    print(f"Right Rotated arr by {k} places: {arr}", end='\n')
    # time = O(n + k + n-k) = O(2*n) = O(n)
    # space = O(1)
    

def left_rotate(arr, k):
    # Left rotate by k places
    # Reverse first k 
    # Reverse remaining n-k
    # Reverse entire arr
    
    print(f"Original arr: {arr}")
    n = len(arr)
    k = k % n
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    print(f"Left Rotated arr by {k} places: {arr}")
    # time = O(k + n-k + n) = O(2*n) = O(n)
    # space = O(1)
    
def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = int(input("Enter the value of k: "))
    # right rotate on the original array
    right_rotate(arr, k)
    print("===================")
    # restore to the original array
    right_rotate(arr, len(arr)-k)
    print("===================")
    # now, left rotate on the original arry
    # NEW: left rotation can also be performed by rotating the entire list first, then rotating LAST k elements and then rotating the remaining first n-k elements.
    left_rotate(arr, k)

if __name__ == '__main__':
    main()
