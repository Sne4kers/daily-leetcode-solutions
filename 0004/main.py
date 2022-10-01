class Solution:
    def findKthElement(nums1, nums2, k):
        if len(nums1) > len(nums2):
            return Solution.findKthElement(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k]
        
        mid1 = (len(nums1))// 2
        mid2 = (len(nums2))// 2
        if nums1[mid1] < nums2[mid2]:
            if k < (mid1 + mid2 + 1):
                return Solution.findKthElement(nums1, nums2[:mid2], k)
            else:
                return Solution.findKthElement(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            if k < (mid1 + mid2 + 1):
                return Solution.findKthElement(nums1[:mid1], nums2, k)
            else:
                return Solution.findKthElement(nums1, nums2[mid2 + 1:], k - mid2 - 1)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        return Solution.findKthElement(nums1, nums2, l // 2) if l % 2 == 1 else (Solution.findKthElement(nums1, nums2, l // 2) + Solution.findKthElement(nums1, nums2, (l - 1)// 2)) / 2

# Optimised solution in order to get proper O(log(min(n, m)))
# Got rid of slices but it's still doing worse for some weird for me reason


class Solution:
    def findKthElement(nums1, nums2, begin_a, end_a, begin_b, end_b, k):
        if end_a - begin_a > end_b - begin_b:
            return Solution.findKthElement(nums2, nums1, begin_b, end_b, begin_a, end_a, k)

        if end_a - begin_a <= 0:
            return nums2[begin_b + k]
        
        mid1 = (end_a - begin_a)// 2
        mid2 = (end_b - begin_b)// 2
        if nums1[begin_a + mid1] < nums2[begin_b + mid2]:
            if k < (mid1 + mid2 + 1):
                return Solution.findKthElement(nums1, nums2, begin_a, end_a, begin_b, begin_b + mid2, k)
            else:
                return Solution.findKthElement(nums1, nums2, begin_a + mid1 + 1, end_a, begin_b, end_b, k - mid1 - 1)
        else:
            if k < (mid1 + mid2 + 1):
                return Solution.findKthElement(nums1, nums2, begin_a, begin_a + mid1, begin_b, end_b, k)
            else:
                return Solution.findKthElement(nums1, nums2, begin_a, end_a, begin_b + mid2 + 1, end_b, k - mid2 - 1)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        l = a + b
        return Solution.findKthElement(nums1, nums2, 0, a, 0, b, l // 2) if l % 2 == 1 else (Solution.findKthElement(nums1, nums2, 0, a, 0, b, l // 2) + Solution.findKthElement(nums1, nums2, 0, a, 0, b,(l - 1)// 2)) / 2