def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13, 15, 15, 19, 24, 25]
    target = 7

    index = binary_search(array, target)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found in the array")
