class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  # will store indices
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)
        
        return result



def main():
    sol = Solution()
    
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Input:", temperatures)
    print("Output:", sol.dailyTemperatures(temperatures))


if __name__ == "__main__":
    main()