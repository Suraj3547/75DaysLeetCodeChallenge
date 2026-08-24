class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        half = (m + n + 1) // 2

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1

            if partition1 < m:
                right1 = nums1[partition1]
            else:
                right1 = float('inf')

            if partition2 < n:
                right2 = nums2[partition2]
            else:
                right2 = float('inf')

            if partition1 > 0:
                left1 = nums1[partition1 - 1]
            else:
                left1 = float('-inf')

            if partition2 > 0:
                left2 = nums2[partition2 - 1]
            else:
                left2 = float('-inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                right = partition1 - 1

            else:
                left = partition1 + 1