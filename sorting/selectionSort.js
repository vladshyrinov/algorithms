// Algorithmic efficiency - O(n^2)

function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let j = i + 1;
        let minIdx = i;
        while (j < arr.length) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
            j++;
        }

        [arr[minIdx], arr[i]] = [arr[i], arr[minIdx]]
    }

    return arr;
}

console.log(selectionSort([5,23,1,45,34, -19, 2]));