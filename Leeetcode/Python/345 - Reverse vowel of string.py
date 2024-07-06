class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            if  s[i] not in vow: 
                i += 1
            if s[j] not in vow:
                j -= 1
            if s[i] in vow and s[j] in vow:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            
        return "".join(s)