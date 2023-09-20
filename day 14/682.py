from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        for s in operations:
            if s.isdigit() or s[1:].isdigit():
                my_stack.append(int(s))
            elif s == '+':
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                summa = num1 + num2

                my_stack.append(num2)
                my_stack.append(num1)
                my_stack.append(summa)
            elif s == 'D':
                num = my_stack.pop()
                my_stack.append(num)
                my_stack.append(num * 2)
            elif s == 'C':
                my_stack.pop()

        return sum(list(my_stack))

print( Solution().calPoints(["5","-2","4","C","D","9","+","+"]) )