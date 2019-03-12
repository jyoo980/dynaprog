# Functions which compute the fibonacci sequence
# i.e. 0 1 1 2 3 5 8 13 21 34 55 ...

# Naive recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

# Dynamic Programming
def fib_dp(n):
    memo = [0 for i in range(0, n + 2)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

# Dynamic Programming - O(1) space
def fib_dp_space(n):
    prev = 0
    curr = 1
    for i in range(0, n):
        tmp = prev
        prev = curr
        curr = curr + tmp
    return prev


def main():
    print(fib(0))
    print(fib(8))
    # print(fib(50)) # takes much too long with naive recursion
    print(fib_memo(0))
    print(fib_memo(8))
    print(fib_memo(50))

    print(fib_dp(0))
    print(fib_dp(8))
    print(fib_dp(50))

    print(fib_dp_space(50))

if __name__ == "__main__":
    main()