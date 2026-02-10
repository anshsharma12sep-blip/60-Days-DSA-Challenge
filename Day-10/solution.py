def move_zeroes(nums):
    pos = 0  # position to place the next non-zero element

    # First pass: move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    # Second pass: fill remaining positions with zeroes
    for i in range(pos, len(nums)):
        nums[i] = 0


# Driver code
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)
