class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output=""
        max_len=0
        for i in range(len(s)):
            if s[i] in output:
                idx=output.index(s[i])
                output=output[idx+1:]
            output+=s[i]
            max_len=max(max_len,len(output))
        return max_len