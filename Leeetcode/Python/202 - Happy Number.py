class Solution:
    def isHappy(self, n: int) -> bool:
        test = []
        while n > 0:
            temp = 0
            while n > 0:
                rem = n%10
                temp += rem*rem
                n = n//10
            if temp in test:
                return False
            else:
                test.append(temp)    
            if temp == 1:
                return True
            n = temp
        return False
        

