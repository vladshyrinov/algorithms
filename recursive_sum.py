def recursive_sum(arr):
    if arr == []:
        return 0
    return arr[0] + recursive_sum(arr[1:])

def main():
    print(recursive_sum([3,2,-1,4,56,1,8]))

if __name__ == "__main__":
    main()

