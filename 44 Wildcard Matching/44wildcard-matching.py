class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Lengths of input and pattern
        m, n = len(s), len(p)

        # dp[i][j] is True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Fill in first row for patterns with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match zero characters (dp[i][j-1])
                    # or one character from s (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # If characters match or pattern has '?'
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
