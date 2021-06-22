impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;

        let len = nums.len();
        let mut map = HashMap::with_capacity(len);
        for i in 0..len {
            if let Some(k) = map.get(&(target - nums[i])) {
                return vec![*k as i32, i as i32];
            }
            map.insert(nums[i], i);
        }
        vec![]
    }
}
