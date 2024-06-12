def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        queryType, x, y = query
        if queryType == 1:
            arr[(x ^ lastAnswer) % n].append(y)
        if queryType == 2:
            elementPosition = (x ^ lastAnswer) % n
            lastAnswer = arr[elementPosition][y % len(arr[elementPosition])]
            answers.append(lastAnswer)

    return answers

if __name__ == '__main__':
    input_queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]
    print(dynamicArray(5, input_queries))