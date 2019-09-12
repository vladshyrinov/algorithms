# Algorithmic efficiency - O(logn)

def binary_search(arr, low, high, item):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    else:
        return -1

def main():
    arr = list(range(4, 100))
    print(binary_search(arr, 0, len(arr) - 1, 50))

if __name__ == "__main__":
    main()
