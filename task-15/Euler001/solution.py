T = int(input())

for t in range(T):
    N = int(input()) - 1
    sum_of_3 = (3 * (N // 3) * (N // 3 + 1)) // 2
    sum_of_5 = (5 * (N // 5) * (N // 5 + 1)) // 2
    sum_of_15 = (15 * (N // 15) * (N // 15 + 1)) // 2
    sum = sum_of_3 + sum_of_5 - sum_of_15
    print(sum)
