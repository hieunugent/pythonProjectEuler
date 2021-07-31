class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def notoverlap(left, right):
            if (left[0] < right[0] and left[1] < right[0]) or (right[0] < left[0] and right[1] < left[0]):
                return True
            return False

        def mergeOverlap(left, right):
            if left[0] <= right[0] and left[1] >= right[1]:
                return left
            elif right[0] <= left[0] and right[1] >= left[1]:
                return right
            elif left[0] < right[0] and left[1] >= right[0]:
                return [left[0], right[1]]
            elif right[0] < left[0] and right[1] >= left[0]:
                return [right[0], left[1]]
        if len(intervals) == 1:
            return intervals
        current = intervals[0]
        result = []
        ispush = False

        for index1, left in enumerate(intervals):
            if index1 == 0:
                continue
            elif notoverlap(current, left):
                result.append(current)
                current = left
                ispush = not ispush
            else:
                current = mergeOverlap(current, left)
                ispush = not ispush
        if ispush:
            result.append(current)

        return result
