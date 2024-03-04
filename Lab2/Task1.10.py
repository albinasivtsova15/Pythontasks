def count_strikes(N, K, strikes):
    strike_days = set()

    for i in range(1, N + 1):
        for j in range(K):
            if (i - strikes[j][0]) % strikes[j][1] == 0 and i % 7 not in {6, 1}:
                strike_days.add(i)
                break

    return len(strike_days)


N, K = map(int, input().split())
strikes = [list(map(int, input().split())) for _ in range(K)]

result = count_strikes(N, K, strikes)
print(result)
