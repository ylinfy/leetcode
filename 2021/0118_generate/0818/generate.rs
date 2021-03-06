impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        // 将无限iter转成有限，gen_pascal_triangle返回一个无限iter
        // 使用take方法，将无限iter转为有限，即取前num_rows个元素组成一个vec<T>, T为vec
        assert!(num_rows >= 0);
        gen_pascal_triangle()
            .take(num_rows as usize)
            .collect()
    }
}

fn gen_pascal_triangle() -> impl Iterator<Item = Vec<i32>> {
    // successors返回一个Successors<T, F>, 是实现了Iterator trait的结构体
    // chain拼接iter, 杨辉三角每一行前后均为1，因此有vec![1].chain(iter()).chain(vec![1])
    // into把所有权移交给调用者
    std::iter::successors(Some(vec![1]), |row| {
        vec![1].into_iter()
            .chain(row.windows(2).map(|v| v.iter().sum()))
            .chain(vec![1].into_iter())
            .collect::<Vec<i32>>()
            .into()
    })
}
