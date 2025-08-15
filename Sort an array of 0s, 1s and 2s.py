from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = []
        ones = []
        twos = []
        for num in nums:
            if num == 0:
                zeros.append(0)
            elif num == 1:
                ones.append(1)
            else:
                twos.append(2)
        
        sorted_array = zeros + ones + twos
        
        for i in range(len(nums)):
            nums[i] = sorted_array[i]
        


        