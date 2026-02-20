class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        vowels="aeiouAEIOU"
        while i<j:
            if (s[i] in vowels):
                if (s[j] in vowels):
                    k=s[i]
                    s[i]=s[j]
                    s[j]=k
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(s)