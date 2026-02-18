class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        strs=""
        for i in s:
            if i.isalnum():
                strs+=i
        rev=strs[::-1]
        if strs==rev:
            return True
        else:
            return False