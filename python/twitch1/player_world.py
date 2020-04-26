
import random

WORLD_ROWS = 2
WORLD_COLS = 3

WORLD_STATE_FREE = 0
WORLD_STATE_EMPTY = 1

world_state = [ [0 for i in range(WORLD_COLS)] for i in range(WORLD_ROWS)
    ]

def print_world_state():
    for row in world_state:
        for position in row:
            print(str(position) +" ",end="")
        print()

def is_world_full():
    for row in world_state:
        for position in row:
            if position == WORLD_STATE_FREE:
                return False
    return True
        
def generate_random_character():
    ''' We use a 5x5 list to mantain world positions.
    We assume:
    - 0 values to mean a free position, 
    - 1 values to mean that a character is there 
    '''
    if is_world_full():
        raise Exception("The world were full")

    # put a character in a random position
    did_i_set_a_new_position = False
    while did_i_set_a_new_position != True:
        row = random.randint(0,WORLD_ROWS-1)
        col = random.randint(0,WORLD_COLS-1)

        if  world_state[row][col] == WORLD_STATE_FREE:
            world_state[row][col] = WORLD_STATE_EMPTY
            did_i_set_a_new_position = True

    print_world_state()
    return


def main():
    while True:
        input("Press enter to generate a new character")
        try:
            generate_random_character()
            print("[+] A new character has been allocated")
        except Exception as e:
            print(e)
            break

if __name__=="__main__":
    main()