impl Solution {
    pub fn sortedArrayToBST(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::build_bst(&nums) 
    } 

    fn build_bst(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty() { return None }
        let mid = nums.len() / 2;
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid],
            left: Self::build_bst(&nums[..mid]),
            right: Self::build_bst(&nums[mid + 1..]),
        })))
    }
}
