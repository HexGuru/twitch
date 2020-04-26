def main():
    # primitive value types

    string = "123 " # String
    integer = 1  # integer
    float_var = 1.5 
    scientific_form = 3e5
    char = 'a'
    boolean = True
    list_var = [1,2,"asd",4]

    # Loops section

    # *for* iteration: it is used to iterate over a finite number of 
    # objects, or over a finite number of iterations
    # the first number in the programmer mind is 0, not 1. 
    # the iterations start from 0.
    print("For loop output\n\n")
    for i in range(10):
        print(i)

    # *while* iteration, is used to repeat an action until a condition is true
    print("While loop output\n\n")
    some_quantity = 5
    while some_quantity > 0:
        print(some_quantity)
        some_quantity= some_quantity-1

    # *functions* one of the tools a programmer has to avoid rewriting its code
    print_nth_digit()

def print_nth_digit():
    numerator = int(input("write in the numerator: "))
    demoninator = int(input("write in the denominator: "))
    index = int(input("what digit do you want to print: "))-1
    result_float = numerator/demoninator
    result=str(result_float)[2:]
    print(result[index])

def stripped_print_nth_digit():
    numerator = int(input("write in the numerator: "))
    demoninator = int(input("write in the denominator: "))
    index = int(input("what digit do you want to print: "))-1
    print(str(numerator/demoninator)[2:][index])

if __name__=="__main__":
    main()