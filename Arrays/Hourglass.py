def hourglass(arr):
    rows = len(arr)
    columns = len(arr[0])
    max_sum = 0
    hourglass_sum = []

    for i in range(rows - 2):
        for j in range(columns - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_total = top + middle + bottom
            hourglass_sum.append(hourglass_total)
            if hourglass_total > max_sum:
                max_sum = hourglass_total


    return max_sum

if __name__ == '__main__':
    input_Array = [[1, 1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0],
                   [1, 1, 1, 0, 0, 0],
                   [0, 0, 2, 4, 4, 0],
                   [0, 0, 0, 2, 0, 0],
                   [0, 0, 1, 2, 4, 0]]

    negative_Array = [[-9, -9, -9, 1, 1, 1],
                      [0, -9, 0, 4, 3, 2],
                      [-9, -9, -9, 1, 2, 3],
                      [0, 0, 8, 6, 6, 0],
                      [0, 0, 0, -2, 0, 0],
                      [0, 0, 1, 2, 4, 0]]

    print('Maximum sum is: {}'.format(hourglass(negative_Array)))
