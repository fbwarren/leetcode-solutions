def coinChange(coins, amount):
    dp = [0] + [amount+1] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1
