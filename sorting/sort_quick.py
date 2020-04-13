# Algorithmic efficiency - O(nlogn) - O(n^2)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = (len(arr) - 1) // 2
        pivot = arr[mid]
        arr = arr[:mid] + arr[mid + 1:]
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater) 

print(quick_sort([1,4,2,7,5,9,2]))
