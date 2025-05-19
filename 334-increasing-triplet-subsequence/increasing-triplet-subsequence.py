class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # length = len(nums)
        # i = 0
        # j = 1
        # k = 2

        # if length < 3:
        #     return False
        

        # while i < length - 2:
        #     j = i + 1
        #     while j < length - 1:
        #         if nums[i] < nums[j]:
        #             k = j + 1
        #             while k < length:
        #                 if nums[j] < nums[k]:
        #                     return True
        #                 k += 1
        #         j += 1
        #     i += 1
                        

        
        # return False

        ith = float(inf)
        jth = float(inf)

        for kth in nums:
            if kth < ith:
                ith = kth
            elif ith < kth and kth < jth:
                jth = kth
            elif kth > jth:
                return True
        
        return False
            