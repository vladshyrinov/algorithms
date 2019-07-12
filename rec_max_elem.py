def rec_max_elem(arr):
    print(arr)
    if arr == []:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] if arr[0] > rec_max_elem(arr[1:]) else rec_max_elem(arr[1:])


def main():
    print(rec_max_elem([1, -2, 10, 50, 3, 34, 51, 6]))

if __name__ == "__main__":
    main()