# https://leetcode.com/problems/decode-string/

from collections import deque

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()  # stack for stashing strings and scalars in op order
        scalar = 0       # initialize neutral storage for both scalars for
        string = ''      #               multiplication as well as strings
        for c in s:
          if c == '[':   # opens clause; push currently tracked items
            stack.append(string)
            stack.append(scalar)
            string = ''  # reset
            scalar = 0   # reinitialize; required by line 24
          elif c == ']': # ends clause; pop deferred items
            num = stack.pop()
            prev_str = stack.pop()
            string = prev_str + num*string # concat current and prior string
            scalar = 0   # reinitialize
          elif c.isdigit(): 
            scalar = scalar*10 + int(c) # accounts for single or multi-digit #
          else:
            string += c
        return string