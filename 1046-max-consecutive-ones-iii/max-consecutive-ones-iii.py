class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, longSeq, result, count, n = 0, 0, 0, 0, len(nums)
        
        for r in range(n):
            if nums[r] == 0:
                count += 1

            while count > k:
                l += 1
                if nums[l - 1] == 0:
                    count -= 1

            longSeq = r - l + 1
            result = max(result, longSeq)
        
        return result

