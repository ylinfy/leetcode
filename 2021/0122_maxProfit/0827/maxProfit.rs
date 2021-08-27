impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.windows(2).filter(|x| x[1] > x[0]).map(|x| x[1] - x[0]).sum()
    }
}
