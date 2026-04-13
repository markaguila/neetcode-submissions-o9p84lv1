import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for n in nums:
            rest = nums[:]
            rest.remove(n)
            product = math.prod(rest)
            products.append(product)
        return products
        