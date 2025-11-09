def merge_sort(array):
    if array is None:
        return []
    arr_copy = array.copy()

    def sort_recursive(arr, left, right):
        if left < right:
            middle = left + (right - left) // 2
            sort_recursive(arr, left, middle)
            sort_recursive(arr, middle + 1, right)
            merge(arr, left, middle, right)

    def merge(arr, left_i, middle_i, right_i):
        left_len = middle_i - left_i + 1
        right_len = right_i - middle_i
        left_array = [0] * left_len
        right_array = [0] * right_len

        for i in range(left_len):
            left_array[i] = arr[left_i + i]
        for j in range(right_len):
            right_array[j] = arr[middle_i + 1 + j]
        i = 0
        j = 0
        k = left_i

        while i < left_len and j < right_len:
            if left_array[i] <= right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < left_len:
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < right_len:
            arr[k] = right_array[j]
            j += 1
            k += 1

    sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy