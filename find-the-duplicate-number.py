# https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        check = set()
        for n in nums:
            if n not in check:
                check.add(n)
            else:
                return n
            
