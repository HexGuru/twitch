import random
def main():
    print("Hello world")


def print_nth_column(matrix,n):
    for row in matrix:
        print(row[n])

if __name__=="__main__":
    matrix = [
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
    ]
    #print_nth_column(matrix,0)

    print()
    print("first 'for' iteration")
    alist = ["abc","hey guys","lol"]
    for i in range(len(alist)):
        print(str(i)+ " " + alist[i])

    print()
    print("second 'for' iteration")
    for element in alist:
        print(element)

    amount = 0
    print()
    print("'while' iteration")
    while amount < 25:
        quantity_produced = random.randint(2,5)
        print("produced "+ str(quantity_produced))
        amount += quantity_produced


    alist = ["abc","hey guys","lol"]
    if "abc" in alist:
        print(True)
    else:
        print(Flase)
    

    matrix = [
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j])+", ", end="")
        print()

    print("only diagonal")
    for i in range(len(matrix)):
        print(matrix[i][i])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                print(str(matrix[i][j])+", ", end="")
            else:
                print(" ,", end="")
        print()

    import numpy as np

    nparray = np.array(matrix)
    print(nparray.diagonal())

