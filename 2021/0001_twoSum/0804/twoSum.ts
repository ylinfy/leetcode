function twoSum(nums: number[], target: number): number[] {
    let len = nums.length;
    let map = new Map();
    for (let j: number = 0; j < len; j++) {
        if (map.has(target - nums[j])) {
            return [map.get(target - nums[j]), j];
        }
        map.set(nums[j], j);
    }
    return [];
}
