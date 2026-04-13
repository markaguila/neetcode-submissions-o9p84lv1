class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def letterCounts(word):
            counts = {}
            for l in word:
                if l in counts:
                    counts[l] += 1
                else:
                    counts[l] = 1
            return counts
        
        def anagrams(a, b):
            if len(a) != len(b) or len(set(a)) != len(set(b)):
                return False
            aCount = letterCounts(a)
            bCount = letterCounts(b)
            for letter in set(a):
                if not bCount.get(letter) or aCount[letter] != bCount[letter]:
                    return False
            return True

        anagramGroups = []
        allWords = strs
        while allWords:
            first = allWords[0]
            anagramGroup = [first]
            for word in allWords[1:]:
                if anagrams(first, word):
                    anagramGroup.append(word)
            for word in anagramGroup:
                allWords.remove(word)
            anagramGroups.append(anagramGroup)
        return anagramGroups

            
        