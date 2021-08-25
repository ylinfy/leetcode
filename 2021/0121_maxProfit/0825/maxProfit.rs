impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut lowest_price, mut max_value) = (std::i32::MAX, 0);
        for &p in prices.iter() {
            lowest_price = core::cmp::min(lowest_price, p);
            max_value = core::cmp::max(max_value, p - lowest_price);
        }
        max_value
    }
}
