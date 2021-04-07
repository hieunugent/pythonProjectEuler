def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      
    if n == 0:
        return nums1
    current = 0
    for i in range(n):
        if nums1[i] > nums2[current]:
            nums1[i], nums2[current] = nums2[current], nums1[i]
        nums2.sort()
    for i in range(n):
        nums1[m+i], nums2[i] = nums2[i], nums1[m+i]
