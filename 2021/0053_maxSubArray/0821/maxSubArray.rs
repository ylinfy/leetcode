impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut pre = 0;
        nums.iter().fold(std::i32::MIN, |acc, &x| {
            pre = core::cmp::max(pre + x, x);
            core::cmp::max(acc, pre)
        })

        nums.iter().fold(
            (0, std::i32::MIN), 
            |mut acc, &x| {
                acc.0 = std::cmp::max(acc.0 + x, x);
                acc.1 = std::cmp::max(acc.0, acc.1);
                acc
        }).1
    }
}
