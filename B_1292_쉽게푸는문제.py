if __name__ == "__main__":
    start, end = map(int, input().split())
    series = [0]
    for i in range(1, 100):
        for j in range(i):
            series.append(i)
    print(sum(series[start:end+1]))
