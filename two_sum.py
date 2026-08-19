class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                
                if nums[i]+nums[j]==target:
                    return [i,j]
                                  
nums=list(map(int,input().split(", ")))
target=int(input())

obj=Solution()
print(obj.twoSum(nums,target))