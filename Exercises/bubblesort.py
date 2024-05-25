def bubble_sort(array):
    n = len(array)
    while n >= 1:
        for x in range(n - 1):
            if array[x] > array[x + 1]:
                temp = array[x + 1]
                array[x + 1] = array[x]
                array[x] = temp
        n -= 1
                
    return array


if __name__ == "__main__":
    arr1 = [6,8,4,2,3,9,1]
    print(bubble_sort(arr1))