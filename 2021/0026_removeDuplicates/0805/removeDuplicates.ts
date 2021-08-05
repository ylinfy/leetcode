function removeDuplicates(nums: number[]): number {
    let slow = 0;
    let len = nums.length;
    for (let fast = 0; fast < len; fast++) {
        if (nums[fast] == nums[slow]) { continue }
        slow += 1;
        nums[slow] = nums[fast];
    }
    return slow + 1;
}
