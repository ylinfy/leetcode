function twoSum(nums: number[], target: number): number[] {
    let map = new Map();
    let len = nums.length;
    for (let i = 0; i < len; i++) {
        if (map.has(target - nums[i])) {
            return [map.get(target - nums[i]), i];
        }
        map.set(nums[i], i);
    }
    return [];
}
