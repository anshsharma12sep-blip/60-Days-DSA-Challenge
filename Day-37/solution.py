class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child


if __name__ == "__main__":
    g = list(map(int, input("Enter greed factors: ").split()))
    s = list(map(int, input("Enter cookie sizes: ").split()))

    obj = Solution()
    print("Maximum children satisfied:", obj.findContentChildren(g, s))