def minMutation(start, end, bank):
    queue = deque()
    queue.appendleft((start, 0))

    while queue:
        curr, steps = queue.pop()
        if curr == end:
            return steps
        for i in range(len(curr)):
            for c in "ACGT":
                mutation = curr[:i] + c + curr[i+1:]
                if mutation in bank:
                    queue.appendleft((mutation, steps+1))
                    bank.remove(mutation)

    return -1
