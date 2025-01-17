class MyStack:

    def __init__(self):
        self._s = []

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        if len(self._s) != 0:
            return self._s.pop()

    def top(self) -> int:
        if len(self._s) != 0:
            return self._s[-1]
        return None

    def empty(self) -> bool:
        if len(self._s) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
