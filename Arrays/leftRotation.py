def leftRotation(d, arr):
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    myArr = [1,2,3,4,5,6,7,8,9]
    print(leftRotation(5, myArr))
