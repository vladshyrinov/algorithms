// Algorithmic efficiency - O(nlogn) - O(n^2)

function quickSort(arr, start, end) {
    if (start < end) {
        const pivotPosition = partition(arr, start, end);
        quickSort(arr, start, pivotPosition - 1);
        quickSort(arr, pivotPosition + 1, end);
    } 

    return arr;
}

function partition(arr, start, end) {
    const pivot = arr[start];
    let i = start + 1;
    for (let j = start + 1; j <= end; j++) {
        if (arr[j] < pivot) {
            [arr[j], arr[i]] = [arr[i], arr[j]];
            i++;
        }
    }
    [arr[start], arr[i - 1]] = [arr[i - 1], arr[start]];
    return i - 1; 
}

const nums = [5, 23, 1, 45, 34, -19, 2, 57, 1, -8, 10, 23, 45, 4, 5, 16];

console.log(quickSort(nums, 0, nums.length));