def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort the intervals based on the start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            # If the start time of the current interval is less than the end time of the previous interval,
            # there is an overlap, so the person cannot attend all meetings
            return False

    return True


# Driver code
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)
