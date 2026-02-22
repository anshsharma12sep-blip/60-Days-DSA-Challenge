class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(token))
        
        return stack[0]


# ---------------- MAIN FUNCTION ----------------
def main():
    sol = Solution()
    
    # Example 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print("Input:", tokens1)
    print("Output:", sol.evalRPN(tokens1))
    
    print()
    
    # Example 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print("Input:", tokens2)
    print("Output:", sol.evalRPN(tokens2))


if __name__ == "__main__":
    main()