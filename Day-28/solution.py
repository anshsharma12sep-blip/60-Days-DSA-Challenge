def twoSum(nums, target):
    num_map = {}  # value -> index
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[nums[i]] = i
    
    return []  # safety


def main():
    # Input from user
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target: "))
    
    result = twoSum(nums, target)
    
    if result:
        print("Indices:", result)
    else:
        print("No valid pair found.")


if __name__ == "__main__":
    main()