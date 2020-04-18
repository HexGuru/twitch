'''
Write a program that checks to see if a 4 4 list is a magic square. 
In a magic square, every row, column, and the two diagonals add up
 to the same value.

'''

def diagonal(matrix):
    '''
    @param matrix: matrix is assumed to be a squared matrix
    '''
    diagonal_elements = []
    for i in range(len(matrix)):
        diagonal_elements.append(matrix[i][i])
    return diagonal_elements

def inverse_diagonal(matrix):
    diagonal_elements = []
    for i in range(len(matrix)-1,-1,-1):
        diagonal_elements.append(matrix[i][len(matrix)-1-i])
    return diagonal_elements

def column(matrix,j):
    ret = []
    for row in matrix:
        ret.append(row[j])
    return ret

def is_magic_square(matrix):
    '''
    @param matrix: matrix assumed to be squared, and with more 
      then a single row
    '''
    value = sum(column(matrix,0))
    for row in matrix:
        if sum(row) != value:
            return False
    for i in range(len(matrix[0])):
        _column = column(matrix,i)
        if sum(_column) != value:
            return False
    if sum(diagonal(matrix)) != value:
        return False
    if sum(inverse_diagonal(matrix)) != value:
        return False
    return True

matrix = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
]

print(diagonal(matrix))
print(inverse_diagonal(matrix))
print(column(matrix,1))

print(is_magic_square(matrix))