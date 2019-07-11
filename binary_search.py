def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if item < arr[mid]:
            high = mid
        elif item > arr[mid]:
            low = mid
        else:
            return mid
    return

def main():
    print(binary_search(list(range(4, 100)), 21))
    
if __name__ == "__main__":
    main()
