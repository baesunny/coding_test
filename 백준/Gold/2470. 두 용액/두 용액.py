n = int(input())
arr = list(map(int, input().split()))

def ZeroLiquid(n, arr):
    arr.sort()

    left, right = 0, n - 1
    closest_sum = float('inf') 
    best_pair = (0, 0)

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            best_pair = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break

    return best_pair

result = ZeroLiquid(n, arr)
print(result[0], result[1])