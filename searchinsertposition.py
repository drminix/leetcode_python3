class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''
         #computational complexity: O(log(N)) -- since its a binary search!
        
        #(0) initialize variables
        left = 0
        right = len(nums)-1
        
        #(1) special cases
      #  if nums[left] > target: return 0
      #  elif nums[right] < target: return len(nums)
        
        
        #(2) perform binary search
        while left<=right:
            mid = (left+right)//2 #overflow can happen
            mid = left + (right-left)//2
            
            if nums[mid] > target:
                 right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                #found!
                return mid
                
        #(3) not found
        return left 
             
        
        