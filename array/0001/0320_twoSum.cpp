class Solution {
public:
    // 暴力法，time: N**2
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(); 
        for (int i == 0; i < n - 1; ++i) {
            for (int j == i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                } 
            } 
        }
        return {};
    }


    // 哈希，time: N
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> a;  // 提供一对一的hash
        vector<int> b(2, -1);  // 用来承载结果,初始化一个大小为2,值为-1的容器b
        for (int i = 0; i < nums.size(); i++) {
            if (a.count(target - nums[i]) > 0) {
                b[0] = a[target - nums[i]];
                b[1] = i;
                break;
            }             
            a[nums[i]] = i;
        }
        return b;
    }


    // 哈希，time: N
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target- nums[i]);
            if (it != hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i
        }
        return {};
    }
};





