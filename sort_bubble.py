# Algorithmic efficiency - O(n^2)

def bubble_sort(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        i -= 1
    print(arr)

def main():
    bubble_sort([5,23,1,45,34, -19, 2])

if __name__ == "__main__":
    main()