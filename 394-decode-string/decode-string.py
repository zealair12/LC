class Solution:
    def decodeString(self, s: str) -> str:
        currentString = ""
        currentNum = 0
        stk = []

        for char in s:
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)
            elif char == '[':
                stk.append((currentNum, currentString))
                currentNum = 0
                currentString = ""
            elif char == ']':
                prevNumber, previousStr = stk.pop()
                currentString = previousStr + (prevNumber * currentString)
            else:
                currentString += char

        return currentString