# Algorithmic efficiency - O(n2)

def selection_sort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx]
    print(arr)

def main():
    selection_sort([5,23,1,45,34])

if __name__ == "__main__":
    main()