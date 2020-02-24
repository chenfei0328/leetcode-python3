import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = collections.Counter(nums1)
        ans = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                ans.append(num)
                counter[num] -= 1
                
        return ans