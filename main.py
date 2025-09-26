# importing Stack to be used in main program
from stack import Stack

# function for selecting a particular Stack
def get_input():
    choices = ["L", "M", "R"]
    while True:
        print("Options: ")
        for i in range(len(choices)):
            print(f"{choices[i]} for {stacks[i].name} Stack")
        # allows for lowercase input, makes user's experience easier
        chosen_stack = input("").upper() 
        if chosen_stack not in choices:
            print("\nInput not a valid Stack. Please try again.\n")
            continue
        for i in range(len(choices)):
            if chosen_stack == choices[i]:
                # returns stack chosen
                return stacks[i] 

print("""
Welcome to the Towers of Hanoi!

The game starts with a stack of disks arranged from largest at the bottom 
to smallest at the top, all on the left tower. 

Your goal is to move the entire stack to the right tower, one disk at a time. 
Rules:
1. You can only move one disk at a time.
2. You can only move the top disk from a tower.
3. No disk may be placed on top of a smaller disk.

Try to solve the puzzle in as few moves as possible!
\n\n""")

# Making sure num_disks is a number and in an appropiate range, simple validation
while True:
    try:
        print("Please make sure number of disks is between 3 and 12 inclusive.")
        print("(We don't want to be here all day if its more than that...)")
        num_disks = int(input("Please input how many disks you would like to use: "))
        correct_range = 3 <= num_disks <= 12
        if not correct_range:
            print("\nNumber not in range. Please try again.\n")
        else:
            print(f"\nYou have selected to use {num_disks} disks! Great choice!\n")
            num_optimal_moves = 2**(num_disks) - 1
            print(f"\nYou can optimally solve this puzzle in {num_optimal_moves} moves...good luck!\n")
            break
    except ValueError:
        print("\nValue input not a number. Please try again.\n")

# preparing the game
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks = [left_stack, middle_stack, right_stack]

# pushing the values from num_disks into the left Stack backwards, to replicate the game visually
for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_moves_made = 0
# the game will end when the right Stack holds all the disks, so this condition is set
while right_stack.size != num_disks:
    for stack in stacks:
        stack.print_items()
    print("\nWhich Stack would you like to move from?: ")
    from_stack = get_input()
    print("\nWhich Stack would you like to move to?: ")
    to_stack = get_input()
    # makes sure both Stack inputs are different
    if from_stack == to_stack: 
        print("\nYou cannot move from a Stack to the same Stack. Please try again.\n")
        continue
    # makes sure you can't move from an empty Stack and waste a move
    if from_stack.is_empty(): 
        print("\nYou cannot move from an empty Stack. Please try again.\n")
        continue
    disk_from = from_stack.peek()
    # ensures the target stack will still be in order, rule of the game
    if to_stack.is_empty() or disk_from < to_stack.peek(): 
        to_stack.push(disk_from)
        from_stack.pop()
        num_moves_made += 1 # move made!
        # moves tracker feature, good for user engagement
        print(f"\nGood move! You have made {num_moves_made} move(s), remember the most optimal amount is {num_optimal_moves}!\n")
    else:
        print("\nInvalid selection, the disks can only be combined in descending order of magnitude. Please try again.\n")

# ending message, game complete!
print(f"\nCongratulations! You completed the game with {num_moves_made} moves!")

    
    

    







