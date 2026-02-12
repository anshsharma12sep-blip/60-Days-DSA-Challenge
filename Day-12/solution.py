def is_anagram(s1, s2):
    # Step 1: Length check
    if len(s1) != len(s2):
        return False

    freq = {}

    # Step 2: Count frequency of characters in s1
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 3: Subtract frequency using s2
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


# Testing
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
