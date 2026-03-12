class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # height of container is limited by shorter wall
            h = min(height[left], height[right])

            # width between the two lines
            width = right - left

            # calculate area
            area = h * width

            # update maximum water stored
            max_water = max(max_water, area)

            # move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


# Example usage
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    
    sol = Solution()
    result = sol.maxArea(height)

    print("Maximum water that can be stored:", result)