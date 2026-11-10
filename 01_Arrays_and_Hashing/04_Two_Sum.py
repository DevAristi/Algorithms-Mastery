class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return []

if __name__ == "__main___":
    sol = Solution()
    print (sol.twoSum([2, 7, 11, 15], 9)) # Expected: [0, 1]
    print (sol.twoSum([3, 2, 4], 6)) # Expected: [1, 2]
    print (sol.twoSum([3, 3], 6)) # Expected: [0 ,1]
    