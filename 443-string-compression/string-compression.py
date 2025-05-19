class Solution:
    def compress(self, chars: List[str]) -> int:
        compStr = ""
        length = len(chars)
        count = 0

        if length == 1:
            return 1

        for i in range(length):
            count += 1
            if i == length - 1 and count == 1:
                compStr += chars[i]
            elif i == length - 1:
                compStr += chars[i] + str(count)
            elif chars[i] != chars[i + 1] and count == 1:  
                compStr += chars[i]
                count = 0     
            elif chars[i] != chars[i + 1]:
                compStr += chars[i] + str(count)
                count = 0

        compStrLen = len(compStr)

        for j in range(compStrLen):
            if j >= length:
                chars.append(compStr[j])
            else:
                chars[j] = compStr[j]

        return compStrLen