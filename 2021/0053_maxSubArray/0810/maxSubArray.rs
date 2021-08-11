impl Solution {
    pub fn max_sub_array(nums: &mut Vec<i32>) -> i32 {
        use std::cmp::max;

        let mut pre = nums[0];
        let mut res = nums[0];
        for i in 1..nums.len() {
            pre = max(nums[i], pre + nums[i]);
            res = max(pre, res);
        }
        res

        /// use iter fold
        use std::cmp::max;
        
        let mut pre = 0;
        nums.iter().fold(
            std::i32::MIN, 
            |acc, &x| {
                pre = max(pre + x, x);
                max(pre, acc)
            }
        )

        /// use iter fold tuple
        use std::cmp::max;

        nums.iter().fold(
            (0, std::i32::MIN),
            |mut acc, &x| {
                acc.0 = max(acc.0 + x, x);
                acc.1 = max(acc.0, acc.1);
                acc
            }
        ).1
    }
}
