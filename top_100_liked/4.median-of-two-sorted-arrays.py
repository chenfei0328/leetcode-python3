class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = len(nums1) + len(nums2)
        even = True if s % 2 == 0 else False
        # index of the last point
        median = s // 2
        
        m, n = 0, 0
        nums = []
        while m + n <= median:
            if m == len(nums1):
                nums.append(nums2[n])
                n += 1
            elif n == len(nums2):
                nums.append(nums1[m])
                m += 1
            else:
                if nums1[m] < nums2[n]:
                    nums.append(nums1[m])
                    m += 1
                else:
                    nums.append(nums2[n])
                    n += 1
        #print(nums)
        if even:
            return (nums[median - 1] + nums[median]) / 2
        else:
            return nums[median]