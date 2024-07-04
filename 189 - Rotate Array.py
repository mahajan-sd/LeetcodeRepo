class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        test = nums.copy()
        if len(nums) == 1 :
            return 0
        for i in range(len(test)):
            if i + k < len(nums):
                nums[(i+k) % len(nums)] = test[i]
            else :
                nums[(i+k) % len(nums)] = test[i]