class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i]
        seen = {} # dictionary of all j indices mapped to their value
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen: # j index we need is already seen, so we know it works with this i index to produce target.
                return [seen[difference], i]
            seen[nums[i]] = i  # this index can be a j index for someone else
            