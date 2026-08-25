class Solution(object):
    def missingMultiple(self, nums, k):
        multiple = k

        while multiple in nums:
            multiple += k

        return multiple