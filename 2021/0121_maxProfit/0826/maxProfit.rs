impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut low_price, mut max_value) = (std::i32::MAX, 0);
        for &p in prices.iter() {
            low_price = std::cmp::min(p, low_price);
            max_value = std::cmp::max(max_value, p - low_price);
        }
        max_value
    }
}
