impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        use std::cmp::max;

        let mut pre = 0;
        let mut sum = std::i32::MIN;
        for i in 0..nums.len() {
            pre = max(pre + nums[i], nums[i]);
            sum = max(pre, sum);
        }
        sum

        use core::cmp::max;
        let mut pre = 0;
        nums.iter().fold(
            std::i32::MIN,
            |acc, &x| {
                pre = max(pre + x, x);
                max(pre, acc)
            }
        )

        use core::cmp::max;
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
