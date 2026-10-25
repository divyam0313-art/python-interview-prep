"""Q18. Coin Change (Minimum Coins)  (Medium | Dynamic Programming (unbounded knapsack))

PROBLEM
Given coin denominations coins (unlimited supply of each) and a target amount, return
the minimum number of coins needed to make that amount, or -1 if it is impossible.

CONCEPT
A greedy approach (always take the biggest coin) FAILS for general denominations, e.g.
coins [1,3,4] and amount 6: greedy gives 4+1+1 = 3 coins but 3+3 = 2 coins. That is the
signal to use DP.

State: dp[a] = minimum coins to make amount a. Recurrence: dp[a] = min(dp[a - c] + 1)
over every coin c <= a. Base: dp[0] = 0. Impossible amounts keep a sentinel 'infinity'
value (amount + 1 is a convenient finite sentinel because no valid answer can need more
coins than the amount itself).

APPROACH
1. dp = [0] + [amount + 1] * amount.
2. For each amount a from 1..amount, try every coin c <= a.
3. dp[a] = min(dp[a], dp[a - c] + 1).
4. Return dp[amount] unless it is still the sentinel -> -1.

COMPLEXITY
Time O(amount x coins), Space O(amount).

EDGE CASES
- amount = 0 -> 0 coins.
- No combination possible -> -1.
- Coin larger than amount is skipped.

FOLLOW-UPS
- Coin Change II: count the number of ways (order does not matter - loop coins
outermost).
- Reconstruct which coins were used.
- Why does BFS also work? (shortest path in an implicit graph).
"""


def coin_change(coins, amount):
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1
