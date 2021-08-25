impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.windows(2).filter(|x| x[1] > x[0]).map(|x| x[1] - x[0]).sum()
        prices.windows(2).map(|x| 0.max(x[1] - x[0])).sum()
    }

}
