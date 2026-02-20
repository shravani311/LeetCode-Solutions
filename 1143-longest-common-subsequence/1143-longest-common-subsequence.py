class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]        
        for i in range(len(text1)-1,-1,-1):     #row from down
            for j in range(len(text2)-1,-1,-1):     #col from down
                if text1[i]==text2[j]:      #if they are same
                    dp[i][j]=dp[i+1][j+1]+1         #get the diagonal of grid value and increment it
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])         #find max of right or below value and place the max value
        return dp[0][0]