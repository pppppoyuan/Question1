import time
import matplotlib.pyplot as plt

# 費氏數列的遞迴實現
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 費氏數列的動態規劃實現
def fib_dynamic(n):
    if n == 0 or n == 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 計算 F(10), F(20), ..., F(100) 的遞迴和動態規劃時間
recursive_times = []
dynamic_times = []
for i in range(10, 101, 10):
    # 計算遞迴時間
    if i >= 50:
        recursive_times.append(2999)  # n>=50的時候把運行時間標成2999
    else:
        start_time = time.time()
        fib_recursive(i)
        recursive_time = time.time() - start_time
        recursive_times.append(recursive_time)

    # 計算動態規劃時間
    start_time = time.time()
    fib_dynamic(i)
    dynamic_time = time.time() - start_time
    dynamic_times.append(dynamic_time)

# 繪製折線圖
plt.plot(range(10, 101, 10), recursive_times, label='Recursive')
plt.plot(range(10, 101, 10), dynamic_times, label='Dynamic')
plt.legend()
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.show()