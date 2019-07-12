# Algorithmic efficiency - O(logn)

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid
        else:
            high = mid
    return

def main():
    idx = binary_search(list(range(4, 100)), 50)
    print(idx)

if __name__ == "__main__":
    main()