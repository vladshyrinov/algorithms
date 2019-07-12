def rec_sum(arr):
    if arr == []:
        return 0
    return arr[0] + rec_sum(arr[1:])

def main():
    print(rec_sum([3,2,-1,4,56,1,8]))

if __name__ == "__main__":
    main()

