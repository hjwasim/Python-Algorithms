def unordered_search(arr, n, data):
    for i in range(n):
        if arr[i] == data:
            return i


def ordered_search(arr, n, data):
    for i in range(n):
        if arr[i] == data:
            return i
        if arr[i] > data:
            return -1
    return -1


if __name__ == '__main__':
    arr = [2, 3, 5, 7, 10]
    found = ordered_search(arr, len(arr), 7)
    print(found)

    arr = [2, 5, 3, 1, 7, 9]
    found = unordered_search(arr, len(arr), 9)
    print(found)
