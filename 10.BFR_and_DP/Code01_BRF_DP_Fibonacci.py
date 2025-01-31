
def Fibonacci(n):
    if n==0 or n==1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2) 


def Fibonacci2(n):
    if n==0 or n==1:
        return 1
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1 
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def main():
    print(Fibonacci(10))
    print(Fibonacci2(10))

if __name__ == "__main__":
    main()