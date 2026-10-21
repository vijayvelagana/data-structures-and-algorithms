class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low >= high:
            return
        p = self.partition(arr, low, high)
        self.quickSort(arr, low, p-1)
        self.quickSort(arr, p+1, high)
    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low
        j = high
        while True:
            while i<=high and arr[i]<=pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i>=j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
