def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack implemented using a list
    stack = []

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if not stack:  # Stack empty but closing bracket found
                return False
            top = stack.pop()
            if bracket_map[char] != top:  # Check for matching bracket
                return False
        else:
            # Ignore other characters (if allowed)
            return False

    # If stack is empty, all brackets matched
    return not stack
if __name__ == "__main__":
    # Test cases
    test_strings = ["()", "()[]{}", "(]", "([)]", "([{}])", "", "{[()]}"]
    
    for s in test_strings:
        if isValid(s):
            print(f'"{s}" → Valid')
        else:
            print(f'"{s}" → Invalid')