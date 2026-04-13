class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        sortedCounts = sorted(counts.items(), reverse=True, key=lambda p:p[1])
        sortedNumbers = [pair[0] for pair in sortedCounts]
        return sortedNumbers[:k]

        