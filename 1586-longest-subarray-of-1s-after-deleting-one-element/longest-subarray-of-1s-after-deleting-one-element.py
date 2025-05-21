class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, longSeq, result, count, n = 0, 0, 1, 0, len(nums)
        
        for r in range(n):
            if nums[r] == 0:
                count += 1

            while count > 1:
                l += 1
                if nums[l - 1] == 0:
                    count -= 1

            longSeq = r - l + 1
            result = max(result, longSeq)
        
        return result - 1