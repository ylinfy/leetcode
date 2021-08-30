impl Solution {
    pub fn sort_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        make_tree(&nums)
    }
}

fn make_tree(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
    if nums.is_empty() { return None }
    let mid = nums.len() / 2;
    Some(Rc::new(RefCell::new(TreeNode {
        val: nums[mid],
        left: make_tree(&nums[..mid]),
        right: make_tree(&nums[mid + 1..]),
    })))
}
