class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k = m-1,n-1,m+n-1

        while i >= 0 and j >= 0:

            if nums1[i]>nums2[j]:

                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1

        while i>=0:
            nums1[k] = nums1[i]
            i-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        return nums1[k]

        

        p1,p2,p = m-1,n-1,m+n-1

        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1
        while p1>=0:
            nums1[p]=nums1[p1]
            p1-=1
            p-=1
        while p2>=0:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1