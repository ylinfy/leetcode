impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        s.bytes().rev().fold((0, 0), |acc, byte| {
            let num = match byte {
                b'I' => 1, b'V' => 5, b'X' => 10, b'L' => 50,
                b'C' => 100, b'D' => 500, b'M' => 1000, _ => -9999,
            };
            (if num < acc.1 {acc.0 - num} else {acc.0 + num}, num)
        }).0
    }
}
