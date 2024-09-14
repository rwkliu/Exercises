def search_matrix(matrix, target):
    if not matrix or not target:
        return False
    
    r = len(matrix[0])
    c = len(matrix)
    start = 0
    end = (r * c) - 1

    while start <= end:
        mid_ind = int((start + end)/ 2)
        mid_val = matrix[int(mid_ind / r)][mid_ind % r]
        print("mid_ind", mid_ind)
        print(mid_val)

        if mid_val == target:
            return True
        if mid_val > target:
            end = mid_ind - 1
        else:
            start = mid_ind + 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
target2 = 13
target3 = 35
target4 = 60

print("Target found: ", search_matrix(matrix, target))
print("Target found: ", search_matrix(matrix, target2))
print("Target found: ", search_matrix(matrix, target3))
print("Target found: ", search_matrix(matrix, target4))
