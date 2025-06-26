class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Função recursiva para dividir e conquistar
        def findMaxSubArray(nums, left, right):
            if left == right: 
                return nums[left]
            
            mid = (left + right) // 2
            
           
            left_max = findMaxSubArray(nums, left, mid)
            right_max = findMaxSubArray(nums, mid + 1, right)
            cross_max = findCrossMax(nums, left, mid, right)
            
            
            return max(left_max, right_max, cross_max)
        
        
        def findCrossMax(nums, left, mid, right):
            
            left_sum = float('-inf')
            temp_sum = 0
            for i in range(mid, left - 1, -1):
                temp_sum += nums[i]
                left_sum = max(left_sum, temp_sum)
            
          
            right_sum = float('-inf')
            temp_sum = 0
            for i in range(mid + 1, right + 1):
                temp_sum += nums[i]
                right_sum = max(right_sum, temp_sum)
            
            
            return left_sum + right_sum
        
        return findMaxSubArray(nums, 0, len(nums) - 1)
