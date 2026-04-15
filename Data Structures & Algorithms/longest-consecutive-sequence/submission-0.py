class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        sortedNums = sorted(nums)
        longestStreak = 0
        currentStreak = 1
        previous = sortedNums[0]
        print(sortedNums)
        for n in sortedNums[1:]:
            if n == previous:
                continue
            elif n == previous + 1:
                currentStreak += 1
            else:
                longestStreak = max(longestStreak, currentStreak)
                currentStreak = 1
            previous = n
        return max(longestStreak, currentStreak)


