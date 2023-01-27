"""How to implement 3 Stacks with one Array? """
class Stack:

    def __init__(self):
        self.pos_1 = 0
        self.pos_2 = 1
        self.pos_3 = 2
        self.stack = [None, None, None]

    def pop_1(self):
        if self.pos_2 - 1 > 0:
            to_ret = self.stack.pop(self.pos_1)
            self.pos_2 -= 1
            self.pos_3 -= 1
        return to_ret

    def push_1(self, value):
        self.stack.insert(self.pos_1, value)
        self.pos_2 += 1
        self.pos_3 += 1
        return None

    def pop_2(self):
        if self.pos_2 - 1 < self.pos_3:
            to_ret = self.stack.pop(self.pos_2)
            self.pos_3 -= 1
        return to_ret

    def push_2(self, value):
        self.stack.insert(self.pos_2, value)
        self.pos_3 += 1
        return None

    def pop_3(self):
        if self.pos_3 - 1 > self.pos_2:
            to_ret = self.stack.pop(self.pos_3)
        return to_ret

    def push_3(self, value):
        self.stack.insert(self.pos_3, value)
        return None

if __name__ == "__main__":
    stack = Stack()
    stack.push_2(22)
    stack.push_1(1)
    stack.push_1(2)
    print (stack.pop_1())
    print (stack.pop_1())
    print (stack.pop_2())