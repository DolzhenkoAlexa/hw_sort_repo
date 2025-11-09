def quick_sort(array):
    if array is None:
        return []
    arr_copy = array.copy()

    def sort_recursive(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            sort_recursive(arr, low, pivot_index - 1)
            sort_recursive(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy