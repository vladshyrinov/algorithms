def rec_elements_count(arr):
    if len(arr) == 0:
        return 0
    return 1 + rec_elements_count(arr[1:])

def main():
    print(rec_elements_count([1,2,3,5,1,2,5,2,3,4]))

if __name__ == "__main__":
    main()
    