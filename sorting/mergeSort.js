// Algorithmic efficiency - O(nlogn)

function merge(leftSide, rightSide) {
    let mergedArr = [], i = 0, j = 0;

    while (i < leftSide.length && j < rightSide.length) {
        if (leftSide[i] < rightSide[j]) {
            mergedArr.push(leftSide[i]);
            i++;
        } else {
            mergedArr.push(rightSide[j]);
            j++;
        }
    }

    return mergedArr
        .concat(leftSide.slice(i))
        .concat(rightSide.slice(j));
}

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const middle = Math.floor(arr.length / 2);
    const leftSide = arr.slice(0, middle);
    const rightSide = arr.slice(middle, arr.length);

    return merge(mergeSort(leftSide), mergeSort(rightSide));
}


const nums = [5, 23, 1, 45, 34, -19, 2, 57, 1, -8, 10, 23, 45, 4, 5, 16];

console.log(mergeSort(nums));
