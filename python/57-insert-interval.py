def insert(self, intervals, newInterval):
    output = []

    for i in range(len(intervals)):
        if newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            return output + [newInterval] + intervals[i:]
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

    output.append(newInterval)
    return output
