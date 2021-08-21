impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut digits = digits;
        let mut i = digits.len() as i32 - 1;
        loop {
            if i < 0 { break } 
            digits[i as usize] = (digits[i as usize] + 1) % 10;
            if digits[i as usize] != 0 { return digits }
            i -= 1;
        }
        digits.insert(0, 1);
        digits
    }
}
