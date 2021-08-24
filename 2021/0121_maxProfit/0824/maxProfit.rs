impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut lowest_price, mut max_profit) = (std::i32::MAX, 0);
        for &p in prices.iter() {
            lowest_price = std::cmp::min(lowest_price, p);
            max_profit = std::cmp::max(max_profit, p - lowest_price);
        }
        max_profit
    }
}
