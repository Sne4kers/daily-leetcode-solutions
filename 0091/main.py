class Solution:
    def numDecodings(self, s: str) -> int:
        dp_a = [0] * (len(s) + 1)
        dp_b = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        else:
            dp_a[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp_b[i+1] = dp_a[i]
                else:
                    return 0
            else:
                two_digit = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')
                if two_digit <= 26:
                    dp_b[i+1] = dp_a[i]
                dp_a[i+1] = dp_a[i] + dp_b[i]
        return dp_b[-1] + dp_a[-1]
