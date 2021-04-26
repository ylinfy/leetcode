use std::collections::HashSet;

impl Solution {
    // 交换
    pub fn find_repeat_number(mut nums: Vec<i32>) -> i32 {
        for i in 0..nums.len() {
            // 由于Rust中索引只支持usize，所以此处将类型转换成usize
            let mut j = nums[i] as usize;

            if i == j { 
                continue;
            }
            if nums[i] == nums[j] {
                return nums[i];
            }
            nums.swap(i, j);
        }
        -1
    }


    // 集合
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut d = HashSet::new();

        for i in nums.iter() {  // 此处遍历的是nums各值的引用
            // 如果已经存在，说明是重复数字，直接返回
            if d.contains(i) {
                return *i;
            } 
            d.insert(*i);
        }
        -1
    }


    // 数组
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut v = vec![false; nums.len()];

        for i in nums.iter() {
            // 所有位置均初始化为false, 当重复索引出现时，即重复数值
            if v[*i as usize] == true {
                return *i;
            }
            v[*i as usize] = true;
        }
        -1
    }
}
