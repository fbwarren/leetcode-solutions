def combinationSum(self, candidates, target):
    output = []

    def dfs(candidates, target, combination):
        if target < 0:
            return
        if target == 0:
            output.append(combination)
            return
        else:
            for i in range(len(candidates)):
                dfs(candidates[i:], target-candidates[i], combination + [candidates[i]])

    dfs(candidates, target, [])
    return output
