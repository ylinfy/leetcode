impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        assert!(row_index >= 0);
        let index = row_index as usize + 1;
        let mut ret = vec![1; index];
        for i in 2..index {
            for j in (1..i).rev() {
                ret[j] += ret[j - 1]; 
            }
        }
        ret

        // method 2
        assert!(row_index >= 0);
        gen_pascal_triangle()
            .skip(row_index as usize)
            .next()
            .unwrap()
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

