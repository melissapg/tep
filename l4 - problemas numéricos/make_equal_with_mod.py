test_cases = int(input())

while test_cases > 0:
    array_length = int(input())
    array = list(map(int, input().split()))
    array.sort()

    if array.count(1) == 0:
        print("YES")
    else:
        if array[0] == 1:
            result = "YES"
            for i in range(0, array_length-1):
                if (array[i+1] - array[i]) == 1:
                    result = "NO"
                    break
            print(result)
        else:
            print("NO")

    test_cases = test_cases - 1
