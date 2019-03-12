import math
import time

infty = math.inf


# Given an integer n representing a cash amount, return the minimum 
# number of coins required to make change using 25, 10, and 1 cent(s).

# Naive recursion
def num_coins(n):
	if n < 0:
		return infty
	if n == 0:
		return 0
	if n > 0:
		return 1 + min(num_coins(n - 25), num_coins(n - 10), num_coins(n - 1))

# With memoization
memo = {}
def num_coins_memo(n):
	if n in memo:
		return memo[n]
	if n < 0:
		memo[n] = infty
	if n == 0:
		memo[n] = 0
	if n > 0:
		memo[n] = 1 + min(num_coins_memo(n - 25), num_coins_memo(n - 10), num_coins_memo(n - 1))

	return memo[n]

def main():
	print(num_coins(10))
	print(num_coins(30))
	print(num_coins(20))
	# print(num_coins(80))

	print(num_coins_memo(10))
	print(num_coins_memo(30))
	print(num_coins_memo(20))
	print(num_coins_memo(80))
	print(num_coins_memo(8000))

if __name__ == "__main__":
	main()



