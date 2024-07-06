class Solution:
    def reverse(self, x: int) -> int:
        if (x > 2147483647) or (x < -2147483648):
            return 0
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        test = list(str(x))
        j = len(test)-1
        i = 0
        while i<j:
            temp = test[i]
            test[i] = test[j]
            test[j] = temp
            j -= 1
            i += 1
        test = int(''.join(test))    
        if flag == 1:
            test = test*(-1)
        if test >  2 ** 31 - 1 or test < -2 ** 31 :
            return 0
        return test
