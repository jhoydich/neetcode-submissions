"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # edge condition needed to set
        # our initial condition
        if len(intervals) == 0:
            return 0

        
        # convert to array of tuples
        # put the first meeting in room one
        self.intervals = sorted([(i.start, i.end) for i in intervals])
        self.meeting_rooms = [[self.intervals[0]]]

        # find first meeting room that can accommodate meeting
        # else add another room
        for i in range(1, len(self.intervals)):
            assigned = False
            meeting = self.intervals[i]
            for room in self.meeting_rooms:
                if meeting[0] > room[-1][0] and meeting[0] >= room[-1][1]:
                    room.append(meeting)
                    assigned = True
                    break
            if assigned == False:
                self.meeting_rooms.append([meeting])
        
        print(self.meeting_rooms)
            
        
        return len(self.meeting_rooms)