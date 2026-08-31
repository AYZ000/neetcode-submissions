class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            # Check if we have already seen the number needed to reach the target
            if diff in seen:
                return [seen[diff], i]
            # If not, add the current number and its index to the dictionary
            seen[num] = i