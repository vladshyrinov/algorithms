# Algorithmic efficiency - O(nlogn) - O(n^2)
count = 0

def quicksort(arr):
    global count
    count += 1
    if len(arr) < 2:
        return arr
    else:
        mid = (len(arr) - 1) // 2
        pivot = arr[mid]
        arr = arr[:mid] + arr[mid + 1:]
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) 

def main():
    # print(quicksort([1,4,2,7,5,9,2]))
    print(quicksort([1,2,3,4,5,6,7]))
    print(count)

if __name__ == "__main__":
    main()
