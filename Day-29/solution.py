from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        
        # Step 1: Count frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Use Min Heap
        min_heap = []
        
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Step 3: Extract result
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        
        return result


# Main function
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    
    sol = Solution()
    print(sol.topKFrequent(nums, k))