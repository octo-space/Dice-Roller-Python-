import random


dise = {
    1: [
        "┌───────┐",
        "│       │",
        "│   •   │",
        "│       │",
        "└───────┘"
    ],
    2: [
        "┌───────┐",
        "│ •     │",
        "│       │",
        "│     • │",
        "└───────┘"
    ],
    3: [
        "┌───────┐",
        "│ •     │",
        "│   •   │",
        "│     • │",
        "└───────┘"
    ],
    4: [
        "┌───────┐",
        "│ •   • │",
        "│       │",
        "│ •   • │",
        "└───────┘"
    ],
    5: [
        "┌───────┐",
        "│ •   • │",
        "│   •   │",
        "│ •   • │",
        "└───────┘"
    ],
    6: [
        "┌───────┐",
        "│ •   • │",
        "│ •   • │",
        "│ •   • │",
        "└───────┘"
    ]
}


def print_dice_face(face):
    for line in face:
        print("        " + line)  


def rolling():
    user_input = input("Roll the dice? (y/n): ")

    while user_input == 'y':
        dice_result = random.randint(1, 6)
        print_dice_face(dise[dice_result])
        user_input = input('Roll again? (y/n): ')

rolling()
