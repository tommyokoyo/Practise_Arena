def arrayManipulation(n, queries):
    diff_arr = [0] * (n+1)

    for query in queries:
        a, b, k = query
        diff_arr[a -1] += k
        if b < n:
            diff_arr[b] -= k

    current_value = 0
    max_value = 0

    for val in diff_arr:
        current_value += val
        if current_value > max_value:
            max_value = current_value

    return max_value

if __name__ == '__main__':
    input_arr = [[1, 2, 100],
                 [2, 5, 100],
                 [3, 4, 100]]

    print(arrayManipulation(5, input_arr))