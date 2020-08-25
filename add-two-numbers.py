# https://leetcode.com/problems/add-two-numbers/

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur = ll = ListNode() # (7 -> 0 -> 8)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            # checks if >= 10 for remainder to add to output
            cur = cur.next
            # itrate down ll
            carry //= 10
            # next base 10 slot to evaluate
        return ll.next
