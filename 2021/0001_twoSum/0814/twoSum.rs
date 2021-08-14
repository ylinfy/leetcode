impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;

        let len = nums.len();
        let mut map = HashMap::with_capacity(len);
        for j in 0..len {
            if let Some(i) = map.get(&(target - nums[j])).copied() {
                return vec![i as i32, j as i32]
            } 
            map.insert(nums[j], j);
        }
        vec![]
    }
}
