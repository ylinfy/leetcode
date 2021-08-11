impl Solution {
    pub fn search_insert(nums: &Vec<i32>, target: i32) -> i32 {
        use std::cmp::Ordering;

        let mut left = 0_i32;
        let mut right = nums.len() as i32 - 1;
        while left <= right {
            let mid = (left + right) / 2;
            match nums[mid as usize].cmp(&target) {
                Ordering::Equal => return mid,
                Ordering::Less => left = mid + 1,
                Ordering::Greater => right = mid - 1
            }
        }
        left


        /// method 2
        match nums.binary_search_by(|mid| mid.com(&target)) {
            Ok(i) => i as i32,
            Err(j) => j as i32
        }

        /// method 3
        nums.binary_search(&target).unwrap_or_else(|x| x) as i32
    }
}
