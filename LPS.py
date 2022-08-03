def longestPalindromeSubseq(self, s: str) -> int:
        t=s[::-1]
        n=len(s)
        m=len(t)
        dp=[[-1 for x in range(m+1)] for y in range(n+1)]
        def rec(ind1,ind2):
            if(ind1<0 or ind2<0):
                return 0
            if(dp[ind1][ind2]!=-1):
                return dp[ind1][ind2]
            if(s[ind1]==t[ind2]):
                dp[ind1][ind2]=1+rec(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(rec(ind1,ind2-1),rec(ind1-1,ind2))
            return dp[ind1][ind2]
        return rec(n-1,m-1)
