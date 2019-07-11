def recursive_sum(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr[0]
    else:
        return arr.pop(arr_len-1) + recursive_sum(arr)

def main():
    print(recursive_sum([3,2,-1,4,56,1,8]))

if __name__ == "__main__":
    main()

