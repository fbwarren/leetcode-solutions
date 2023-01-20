public int[][] Insert(int[][] intervals, int[] newInterval) {
    List<int[]> output = new List<int[]>();

    // add all intervals that come before the new interval
    int i = 0;
    while (i < intervals.Length && intervals[i][1] < newInterval[0]) {
        output.Add(intervals[i]);
        i++;
    }

    while (i < intervals.Length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.Min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.Max(newInterval[1], intervals[i][1]);
        i++;
    }
    output.Add(newInterval);

    while (i < intervals.Length) {
        output.Add(intervals[i]);
        i++;
    }

    return output.ToArray();
}
