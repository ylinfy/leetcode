function twoSum(nums: number[], target: number): number[] {
    let len = nums.length;
    let map = new Map();
    for (let i: number = 0; i < len; i++) {
        if (map.has(target - nums[i])) {
            return [map.get(target - nums[i]), i];
        }
        map.set(nums[i], i);
    }
    return []
}
