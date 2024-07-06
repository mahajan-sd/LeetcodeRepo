class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = list(s.lower())
        sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
        for i in test:
            if i not in sample:
                test.remove(i)
        if len(test) == 0 :
            return True
        test = [x for x in test if x in sample] 
        print(test) 
        i, j = 0, len(test)-1
        while i < j:
            if test[i] != test[j]:
                return False
            i += 1
            j -= 1     
        return True
