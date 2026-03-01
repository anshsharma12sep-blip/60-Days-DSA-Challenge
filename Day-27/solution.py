class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
       
        if k <= 0:
            return False
        
        last_seen = {}
        
        for i in range(len(nums)):
            current_value = nums[i]
            
          
            if current_value in last_seen:
            
                if i - last_seen[current_value] <= k:
                    return True
            
            
            last_seen[current_value] = i
        
        return False


if __name__ == "__main__":
    solution = Solution()
    
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    k = int(input("Enter value of k: "))
    
    result = solution.containsNearbyDuplicate(nums, k)
    
    if result:
        print("True")
    else:
        print("False")