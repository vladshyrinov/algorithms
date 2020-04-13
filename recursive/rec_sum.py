# Algorithmic efficiency - O(n)

def rec_sum(arr):
    if arr == []:
        return 0
    return arr[0] + rec_sum(arr[1:])

print(rec_sum([3,2,-1,4,56,1,8]))


