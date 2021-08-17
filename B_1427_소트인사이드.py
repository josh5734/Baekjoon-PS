if __name__ == "__main__":
    number = list(map(int, input()))
    number.sort(reverse=True)

    for x in map(str, number):
        print(x, end="")
