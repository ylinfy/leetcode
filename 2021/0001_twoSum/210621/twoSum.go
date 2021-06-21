func twoSum(nums []int, target int) []int {
    hashTable := map[int]int {}
    for i, n := range nums {
        if p, ok := hashTable[target - n]; ok {
            return []int{p, i}
        }
        hashTable[n] = i
    }
    return nil
}
