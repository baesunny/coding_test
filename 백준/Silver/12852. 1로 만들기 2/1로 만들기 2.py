n = int(input())

def make_1(n):
    min = [0] * (n + 1)
    previous_number = [0] * (n + 1)
    for current in range(2, n + 1):
        min[current] = min[current - 1] + 1
        previous_number[current] = current - 1

        if current % 2 == 0 and min[current // 2] + 1 < min[current]:
            min[current] = min[current // 2] + 1
            previous_number[current] = current // 2

        if current % 3 == 0 and min[current // 3] + 1 < min[current]:
            min[current] = min[current // 3] + 1
            previous_number[current] = current // 3
    print(min[n])

    path = []
    while n != 0:
        path.append(n)
        n = previous_number[n]

    print(" ".join(map(str, path)))

make_1(n)