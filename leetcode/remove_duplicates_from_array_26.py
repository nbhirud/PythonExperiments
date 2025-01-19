# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        readPtr = 0
        putPtr = 1
        while readPtr < len(nums)-1:
            # if nums[readPtr] == nums[readPtr + 1]:
            #     readPtr += 1
            if nums[readPtr] < nums[readPtr + 1]:
                nums[putPtr] = nums[readPtr + 1]
                putPtr += 1
            readPtr += 1
            # print(f"nums = {nums}, readPtr = {readPtr}, putPtr = {putPtr}")
        return putPtr
            
if __name__ == '__main__':
    # nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution().removeDuplicates(nums)
    print(s, nums)