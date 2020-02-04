"""
155. Min Stack
@Level: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        if self.s is None:
            return 0
        return self.s[len(self.s)-1]

    def getMin(self) -> int:
        m = float('inf')
        for i in self.s:
            if i < m:
                m = i
        return m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()