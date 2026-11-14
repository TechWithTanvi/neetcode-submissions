class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i= 0

        for i in range(len(nums)):
            j = 0
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    if i<j: 
                        return [i,j]
                    else: 
                        return [j, i]

#Time: O(n^2) Space: O(1)
        
        #seen = {}
        #for i, num in enumerate(nums):
        #    diff= target-num
        #    if diff in seen:
        #       return(seen[diff],i)
        #    seen[num] = i
#Time O(n) SpaceO(n)

        