// Algorithmic efficiency - O(n)

function maxSubarraySum (nums) {
    let currentIntervalMax = nums[0];
    let max = nums[0];

    for (let i = 1; i < nums.length; i++) {
        const current = nums[i];
        currentIntervalMax = Math.max(0, current + currentIntervalMax);
        max = Math.max(max, currentIntervalMax);
    }

    return max;
}

console.log(maxSubarraySum([1, -7, 9, 6, -3, 5, 4]));