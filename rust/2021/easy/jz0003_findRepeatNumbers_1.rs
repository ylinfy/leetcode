use std::collections::HashSet;


impl Solution {
    pub fn find_repeat_number(mut nums: Vec<i32>) -> i32 {
        for i in 0..nums.len() {
            let j = nums[i] as usize;

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

    
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut d = HashSet::new();
        
        for i in nums.iter() {
            if d.contains(i) {
                return *i;
            }
            d.insert(*i);
        }
        println!("{}", nums);
        -1
    }


    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut v = vec![false; nums.len()];

        for i in nums.iter() {
            if v[*i as usize] == true {
                return *i;
            }
            v[*i as usize] = true;
        }
        println!("{}", nums);
        -1
    }
}
