import math
#https://leetcode.com/problems/split-array-largest-sum/description/
class Solution:
    def split(self,nums,cuts,mx):
        acc=0
        for num in nums:
            if num>mx:
                return False
            elif acc+num<=mx:
                acc=acc+num
            else:
                cuts=cuts-1
                acc = num
                if (cuts < 0):
                    return False
        return True
            
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left=0
        right=0
        for num in nums:
            left=max(left,num)
            right+=num
        while left<right:
            mid=(left+right)/2
            ft=self.split(nums,m-1,mid)
            if ft:
                right=mid
            else:
                left=mid+1
        return math.floor(left)
    