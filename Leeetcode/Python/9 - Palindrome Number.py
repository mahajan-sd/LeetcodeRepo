class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        j = len(test)-1
        for i in range(len(test)):
            if test[i] != test[j]:
                return False
            j = j-1
        return True
    


    