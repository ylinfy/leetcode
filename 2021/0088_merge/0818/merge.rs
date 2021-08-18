impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let (mut m, mut n) = (m as usize, n as usize);
        let mut tail = m + n - 1;
        loop {
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
