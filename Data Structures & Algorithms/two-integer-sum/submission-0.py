class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for firstIndex in range(len(nums)):
            first = nums[firstIndex]
            mustFind = target - first
            for restIndex in range(firstIndex + 1, len(nums)):
                if nums[restIndex] == mustFind:
                    return [firstIndex, restIndex]

