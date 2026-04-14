class Solution:
    def isPalindrome(self, s: str) -> bool:
        capsOnly = s.upper()
        def isAlphanumeric(n):
            return n in "ABCDDEFGHIJKLMOPQRSTUVWXYZ0123456789"
        alphaNumericOnly = [l for l in list(capsOnly) if isAlphanumeric(l)]
        return alphaNumericOnly == alphaNumericOnly[::-1]