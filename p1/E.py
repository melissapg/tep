def minimal_sum_of_distances(relatives, houses):
    houses.sort()
    min_sum = 0

    if relatives % 2:
        # obtém o elemento central da lista de casas
        mid_house = houses[relatives//2]
    else:
        # obtém a média dos dois elementos centrais da lista de casas
        mid_house = (1/2) * (houses[(relatives//2) - 1] + houses[relatives//2])

    # obtém a distância entre a casa central e todas as casas da lista
    for house in houses:
        min_sum += abs(house - mid_house)

    return int(min_sum)


for _ in range(int(input())):
    relatives_houses = list(map(int, input().split()))
    relatives = int(relatives_houses[0])
    houses = relatives_houses[1:]

    print(minimal_sum_of_distances(relatives, houses))
