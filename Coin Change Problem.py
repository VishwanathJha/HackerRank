import sys


def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]


if __name__ == '__main__':           
    N, M = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))
    
    print(changes(N,C))
   
   
