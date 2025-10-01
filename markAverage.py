n = int(input())
scores = list(map(float, input().split()))
maxScores = (max(scores))
minScores = (min(scores))
# dùng list [] mới dùng được len
filterScores = [s for s in scores if s != maxScores and s != minScores]
markAverage = sum(filterScores) / len(filterScores)
print(f"{markAverage:.2f}")