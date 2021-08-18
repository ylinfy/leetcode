impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::make_tree(&nums)
    }

    fn make_tree(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty() { return None }
        let mid = nums.len() / 2;
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid],
            left: Self::make_tree(&nums[..mid]),
            right: Self::make_tree(&nums[mid + 1..]),
        })))
    }
}
