function removeElement(nums: number[], val: number): number {
    let slow = 0;
    let len = nums.length;
    for (let fast = 0; fast < len; fast++) {
        if (nums[fast] == val) {
            continue;
        }
        nums[slow] = nums[fast];
        slow += 1;
    }
    return slow;
}
