#User function Template for python3

def helper(s, left, right):
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]

class Solution:
    def longestPalin(self, s):
        # code here
        res = ""
        for i in range(len(s)):
            test = helper(s, i, i)
            if len(test) > len(res):
                res = test
            test = helper(s, i, i + 1)
            if len(test) > len(res):
                res = test
        return res if len(res) > 1 else s[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()
