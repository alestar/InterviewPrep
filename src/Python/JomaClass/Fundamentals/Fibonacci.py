def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fib_recur(n):
    a, b = 0, 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


def fib_recur_memo(memo, n):
    if n in memo:
        return memo[n]
    else:
        ans = fib_recur_memo(n - 1) + fib_recur_memo(n - 2)
        memo[n] = ans
        return ans

print(fib_recur(0))
print(fib_recur(1))
print(fib_recur(2))
print(fib_recur(3))
print(fib_recur(4))
print(fib_recur(5))


