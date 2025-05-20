class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Solve problem like you're finding largest possible Area
        # The only possibility of the Area being more is the length being higher,
        # since the width keeps decreasing
        # But in the end, it will only check for the highest area found amongst all 
        # of this, and record as the result
        # only moving the pointer with lesser height can give a better result
        n = len(height)
        l,r = 0, n - 1
        result = 0

        while l < r:
            length = min(height[l], height[r])
            width = r - l

            if length == height[r]:
                r -= 1
                while l < r and height[r] < length:
                    r -= 1
            else:
                l += 1
                while l < r and height[l] < length:
                    l += 1

            result = max(result, length * width)

        return result

