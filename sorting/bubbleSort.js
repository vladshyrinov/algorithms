// Algorithmic efficiency - O(n^2)

function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] > arr[j]) {
                const temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            } 
        }
    }
    return arr;
}

console.log(bubbleSort([5,23,1,45,34, -19, 2]));