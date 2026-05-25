"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted([(i.start, i.end) for i in intervals])
        res = True
        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            curr = intervals[i]

            if curr[0] > prev[0] and curr[0] >= prev[1]:
                continue
            res = False
            break

        return res
