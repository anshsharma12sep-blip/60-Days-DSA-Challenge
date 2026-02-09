def max_subarray_sum(arr):
    # Handle case when array has at least one element
    current_sum = arr[0]
    max_sum = arr[0]

    # Traverse from second element
    for i in range(1, len(arr)):
        # Either start new subarray or extend existing one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# --------- Example Usage ----------
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(result)
