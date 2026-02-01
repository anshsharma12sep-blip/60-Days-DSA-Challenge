from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            store = target - nums[i]
            if store in mp:
                return [mp[store], i]

            mp[nums[i]] = i

# Optional test
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))  # Output: [0, 1]
