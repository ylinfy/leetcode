function removeElements(nums: number[], val: number): number {
    let len: number = nums.length;
    let slow: number = 0;
    for (let fast: number = 0; fast < len; fast++) {
        if (nums[fast] == val) {
            continue;
        }
        nums[slow] = nums[fast];
        slow += 1
    }
    return slow;
}
