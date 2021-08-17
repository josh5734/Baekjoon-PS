if __name__ == "__main__":
    score = list(input())
    length = len(score)
    answer = "LUCKY" if sum(
        map(int, score[:(length//2)])) == sum(map(int, score[length//2:])) else "READY"
    print(answer)
