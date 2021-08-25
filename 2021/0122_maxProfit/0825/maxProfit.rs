impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_value = 0;
        for i in 1..prices.len() {
            let delta = prices[i] - prices[i - 1];
            if delta > 0 {
                max_value += delta;
            }
        }
        max_value

        // method 2
        prices.windows(2).map(|x| 0.max(x[1] - x[0])).sum()

        // method 3
        prices.windows(2).filter(|x| x[1] > x[0]).map(|x| x[1] - x[0]).sum()
    }
}
