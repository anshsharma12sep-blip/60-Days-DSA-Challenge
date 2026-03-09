class Solution:
    def findMaxAverage(self, nums, k):
        # Step 1: Calculate sum of first window
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]        # add next element
            window_sum -= nums[i - k]    # remove element leaving the window
            
            if window_sum > max_sum:
                max_sum = window_sum

        # Step 3: Return maximum average
        return max_sum / k


# Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4

solution = Solution()
result = solution.findMaxAverage(nums, k)

print("Maximum Average:", result)