def longest_substring_without_repeating(s):
    # Set to store characters in the current window
    char_set = set()

    left = 0
    max_length = 0

    # Traverse string with right pointer
    for right in range(len(s)):

        # If duplicate character found, shrink window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character to set
        char_set.add(s[right])

        # Update maximum length
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


def main():
    # Sample test cases
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abcdef",
        "abba"
    ]

    for s in test_cases:
        result = longest_substring_without_repeating(s)
        print(f"Input: {s}")
        print(f"Longest substring length: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()