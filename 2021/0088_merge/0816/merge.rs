impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut m = m as usize;
        let mut n = n as usize;
        let mut tail = m + n - 1;
        loop {
            // 只要nums2遍历完，即可跳出循环，剩下的nums1是按要求排序好的
            if n == 0 { break }
            if m == 0 || nums1[m - 1] < nums2[n - 1] {
                nums1[tail] = nums2[n - 1];
                if n > 0 { n -= 1 }
            } else {
                nums1[tail] = nums1[m - 1];
                if m > 0 { m -= 1 }
            }
            tail -= 1;
        }
    }
}
