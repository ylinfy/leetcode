function removeDuplicates(nums: number[]): number {
    let len: number = nums.length;
    let slow: number = 0;
    for (let fast: number = 0; fast < len; fast++) {
        if (nums[fast] == nums[slow]) {
            continue;
        }
        slow += 1;
        nums[slow] = nums[fast];
    }
    return slow + 1;
}
