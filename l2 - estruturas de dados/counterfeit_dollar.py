def counterfeit_dollar(lines):
    lighter = set([coin for coin in "ABCDEFGHIJKL"])
    heavier = set([coin for coin in "ABCDEFGHIJKL"])

    for coins_left, coins_right, answer in lines:
        if answer == "even":
            lighter = lighter.difference(coins_left).difference(coins_right)
            heavier = heavier.difference(coins_left).difference(coins_right)
        elif answer == "up":
            lighter = lighter.intersection(coins_right).difference(coins_left)
            heavier = heavier.intersection(coins_left).difference(coins_right)
        else:
            lighter = lighter.intersection(coins_left).difference(coins_right)
            heavier = heavier.intersection(coins_right).difference(coins_left)
    
    if len(lighter):
        coin = lighter.pop()
        answer = "light"
    else:
        coin = heavier.pop()
        answer = "heavy"
    
    return coin, answer


def main():
    n = int(input())

    for _ in range(n):
        lines = []
        for _ in range(3):
            coins_left, coins_right, answer = input().split()
            lines.append((set([coin for coin in coins_left]),
                        set([coin for coin in coins_right]),
                        answer))

        coin, answer = counterfeit_dollar(lines)
        print(f"{coin} is the counterfeit coin and it is {answer}.")


if __name__ == '__main__':
    main()
