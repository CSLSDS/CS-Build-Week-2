# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        xset = set()
        for ixx, x in enumerate(nums):
            xset.add(x)
            if target - x in xset:
                match = [ix for ix, v in enumerate(nums) if v == target-x][0]
                if match != ixx:
                    return match, ixx
