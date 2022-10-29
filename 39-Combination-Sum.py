def combinationSum(self, candidates, target):
    output = []

    def dfs(candidates, target, path):
        if target < 0:
            return
        if target == 0:
            output.append(path)
            return
        else:
            for i in range(len(candidates)):
                dfs(candidates[i:], target-candidates[i], path + [candidates[i]])

    dfs(candidates, target, [])
    return output
