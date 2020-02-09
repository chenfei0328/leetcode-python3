class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValue = None

    def push(self, x: int) -> None:
        if self.minValue == None or x <= self.minValue:
            self.stack.append(self.minValue)
            self.minValue = x            
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            top = self.stack[-1]
            self.stack.pop()
            if top == self.minValue:
                self.minValue = self.stack[-1]   
                self.stack.pop()
            if len(self.stack) == 0:
                self.minValue = None
            
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return self.minValue