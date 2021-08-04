impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        /// use lib method
        // nums.dedup();
        // nums.len() as i32
        match nums.is_empty() {
            true => 0,
            _ => {
                let mut slow = 0;
                for fast in 0..nums.len() {
                    if nums[fast] == nums[slow] {
                        continue
                    }
                    slow += 1;
                    nums[slow] = nums[fast];
                }
                (slow + 1) as i32
            }
        }
    }
}
