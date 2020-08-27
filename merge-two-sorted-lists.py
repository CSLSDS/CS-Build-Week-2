# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        cur = ll = ListNode() # init merged list to return
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    l1 = l1.next
                elif l1.val > l2.val:
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                    l2 = l2.next
                else:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                    l1 = l1.next
                    l2 = l2.next
            elif l1:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            elif l2:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
        return ll.next

