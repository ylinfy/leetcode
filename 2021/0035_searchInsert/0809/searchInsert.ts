function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = left + ((right - left) >> 1);
        if (nums[mid] == target) { return mid }
        if (nums[mid] > target) { right = mid - 1 }
        else { left = mid + 1}
    }
    return left;
}
