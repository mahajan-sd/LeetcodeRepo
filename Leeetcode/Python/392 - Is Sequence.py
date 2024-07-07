class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:  
            return True
        if len(t) == 0:
            return False    
        while i < len(t):
            if t[i]==s[j]:
                if j==len(s)-1:
                    return True
                j += 1        
            i += 1
        return False