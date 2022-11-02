def canCompleteCircuit(gas, cost):
    start = 0
    total, curr = 0, 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]
        if curr < 0:
            start = i + 1
            curr = 0

    if total < 0:
        return -1
    return start
