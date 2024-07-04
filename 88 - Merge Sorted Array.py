class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)):
            if i >= m:
                nums1.pop(-1)
        for i in range(len(nums2)):
            if i >= n:
                nums2.pop(-1)        
        nums1.extend(nums2)
        nums1.sort()