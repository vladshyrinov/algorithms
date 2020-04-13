# Algorithmic efficiency - O(n)

def rec_elems_count(arr):
    if len(arr) == 0:
        return 0
    return 1 + rec_elems_count(arr[1:])

print(rec_elems_count([1,2,3,5,1,2,5,2,3,4]))

    