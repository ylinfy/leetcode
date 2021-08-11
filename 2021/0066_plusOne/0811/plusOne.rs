impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut tmp = digits;
        let mut i = tmp.len() as i32 - 1;
        loop {
            if i < 0 { break }
            let j = i as usize; // index must be usize type
            tmp[j] += 1;
            tmp[j] %= 10;
            if tmp[j] != 0 {
                return tmp
            }
            i -= 1
        }
        tmp.insert(0, 1);
        tmp
    }
}
