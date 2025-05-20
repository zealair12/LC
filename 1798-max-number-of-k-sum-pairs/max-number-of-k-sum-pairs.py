class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        length = len(nums)
        left = 0
        right = length - 1
        oper = 0

        while left < right:
            if not nums:
                break
            i = nums[left]
            j = nums[right]

            total = i + j

            if total == k:
                oper += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
        
        return oper
            