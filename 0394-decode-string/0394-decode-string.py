class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        num=0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == "[":
                num_stack.append(num)
                num=0
                str_stack.append(char)
            elif char == "]":
                str = ""
                while str_stack and str_stack[-1] != "[":
                    str = str_stack.pop() + str
                str_stack.pop()
                times = int(num_stack.pop())
                str *= times
                str_stack.append(str)
            else:
                str_stack.append(char)
        return "".join(str_stack)
