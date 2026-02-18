class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        base=strs[0]
        for i in range(len(base)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != base[i]:
                    return base[:i]
        return base
            