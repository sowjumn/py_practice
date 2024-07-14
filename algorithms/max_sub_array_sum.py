class MaxSubArraySum:
    def run(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        max_current = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            max_current = max(nums[i],max_current+nums[i])
            if max_sum < max_current:
                max_sum = max_current
            
        return max_sum
    
nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [5,4,-1,7,8]
solution = MaxSubArraySum()
result_1 = solution.run(nums_1)
result_2 = solution.run(nums_2)
print(result_1)
print(result_2)