# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        '''
        initialize your data structure here
        '''
        self.queue = []
        self.stack = []

    def push(self, x):
        '''
        push element x to back of queue
        :type x: int
        :rtype: None
        '''
        self.queue.append(x)

    def pop(self):
        '''
        removes the element from in front of queue and returns that element
        :rtype: int
        '''
        while self.queue:
            self.stack.append(self.queue.pop())
        pop = self.stack.pop()
        while self.stack:
            self.queue.append(self.stack.pop())
        return pop

    def peek(self):
        '''
        get the front element
        :rtype: int
        '''
        while self.queue:
            self.stack.append(self.queue.pop())
        frontelem = self.stack[-1]
        while self.stack:
            self.queue.append(self.stack.pop())
        return frontelem

    def empty(self):
        '''
        returns whether the queue is empty
        :rtype: bool
        '''
        return (not self.queue) and (not self.stack)
