class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        def letterCounts(word):
            counts = {}
            for letter in word:
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
            return counts
        sCount = letterCounts(s)
        tCount = letterCounts(t)
        for letter in set(s):
            if not tCount.get(letter) or sCount[letter] != tCount[letter]:
                return False
        return True