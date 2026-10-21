def binarySearch(mylist, target):
    left = 0
    right = len(mylist)-1
    while left<=right:
        mid = (left+right) // 2
        if mylist[mid] == target:
            return mid
        elif target < mylist[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1
     
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 13

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")
