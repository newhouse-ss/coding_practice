"""
素数判定
1~10000の素数 (prime numbers) を表示してください
例 2, 3, 5, 7, 11, 13
prime number: only dividable by 1 and itself, except 1.

双子素数
1~10000の双子素数を表示してください
差が2の素数のペアを双子素数と言います
例 (3, 5), (5, 7), (11, 13)
1問目の続きで実装して大丈夫です
"""
def is_prime(num):
    # time-complexity: 
    if num <= 1:
        return False
    if num <= 3:
        return True
    # even
    if num % 2 == 0 or num % 3 == 0:
        return False 
    # when n >= 5
    i = 5
    while i * i <= num:
        # O(n ** 0.5)
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    
    return True

res = []

for i in range(10001):
    if is_prime(i):
        res.append(i)

print(res)

# sliding-window-fixed-size
n = len(res)
res_2 = []
for r in range(1, n):
    #O(n)--iteration for n times.
    if res[r] - res[r-1] == 2:
        res_2.append((res[r-1], res[r]))

print(res_2)
# max(O(n**0.5), O(n))-->O(n)