# [322. Coin Change](https://leetcode.com/problems/coin-change/)

**Main Idea**  
This is a dynamic programming problem. I think a bottoms up approach is easiest to understand.  
In a bottoms up approach, we start at the smallest case and work our way upward.  
For this problem specifically, have an array `dp` that will keep track of the least amount of coins needed to create all the amounts up to `amount`.  

**Algorithm**  
We initialize our dp array that is the size of amount plus one.  
We know that we need zero coins to reach an amount of zero, so we initialize `dp[0] = 0`.  
Since the minimum value a coin can be is 1, we know that we'll never get an answer that is greater than `amount`. Because of this, we initialize every other element to `amount+1` to serve as a place holder.  
Then, we iterate through each value between 1 and `amount`, checking to see if there's a valid entry in `dp` for our current amount minus the coin we're trying.  
If there *is* a valid entry, we check to see if it's less than our current minimum change for our current value.  
We do this for every amount and then return `dp[amount]` only if it's less than the value we initialized it to (meaning we actually found some solution).

```python
def coinChange(coins, amount):
    dp = [0] + [amount+1] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1
```

**Time complexity**  
$O(n \cdot m)$ where $n$ is `amount` and $m$ is `len(coins)`

**Space complexity**  
$O(m)$ for `dp`
