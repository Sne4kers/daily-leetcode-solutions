class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = (0, 0)
        last_len = 0
        for i in range(len(s)):
            single_middle = Solution.make_center(s, i, i)
            if single_middle[1] - single_middle[0]  + 1 > last_len:
                result = single_middle
                last_len = result[1] - result[0] + 1
            single_middle = Solution.make_center(s, i, i-1)
            if single_middle[1] - single_middle[0]  + 1 > last_len:
                result = single_middle
                last_len = result[1] - result[0] + 1
                    
        return s[result[0]:result[1] + 1]    
                
    def make_center(s, begin, end):
        while(begin != 0 and end != len(s) - 1 and s[begin - 1] == s[end + 1]):
            begin -= 1
            end += 1
        return (begin, end)
