impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        assert!(num_rows >= 0);
        gen_pascal_triangle()
            .take(num_rows as usize)
            .collect()
    }
}

fn gen_pascal_triangle() -> impl Iterator<Item = Vec<i32>> {
    std::iter::successors(Some(vec![1]), |row| {
        vec![1].into_iter()
            .chain(row.windows(2).map(|v| v.iter().sum()))
            .chain(vec![1].into_iter())
            .collect::<Vec<i32>>()
            .into()
    })
}
