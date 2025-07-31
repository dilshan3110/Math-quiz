import random


def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    print('''

    **** Instructions ****

    To begin, choose the number of questions you would like to do
    The answers will be rounded to the nearest whole for you
    This quiz will include the following type of basic math questions

     - Addition
     - Subtraction
     - Multiplication
     - Division

    Good luck on the quiz.
        ''')


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"
        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)



def get_operations():
    print("Choose operations you want to be tested on in this quiz")
    print("Press + for Addition Questions, - For Subtraction Questions, * For Multiplication Questions, / For Division Questions")
    print("Press <enter> for all operations")
    # operations that can be used/valid
    valid_ops = ["+", "-", "*", "/"]
    while True:
        response = input("Your choice: ").replace(" ", "")
        if response == "":
            return valid_ops
        selected = response.split(",")
        if all(op in valid_ops for op in selected):
            return selected
        else:
            print("invalid choice, try enter a valid operation from the following list, +,-,*,/or just press <enter>")

def generate_question(ops):
    operation = random.choice(operation_list)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if operation == '-':
        if a < b:
            a, b = b, a
        answer = a - b
    if operation == '+':
        answer = a + b
    if operation == '/':
        answer = a
        a = a * b
    if operation == '*':
        answer = a * b
    question = (f"{a} {operation} {b}")
    return question, answer


rounds_played = 0
correct_count = 0
incorrect_count = 0
questions_asked = 0
mode = "Regular"

operation_list = ['+', '-', '/', '*']
game_history = []

# Main Routine
print("Welcome to Math Quiz\n")

want_instructions = string_checker("Do you want to see instructions? ")
if want_instructions == "yes":
    instructions()

num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 999999999999999999

# Game loop starts here
while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()
    question, correct_answer = generate_question(operation_list)
    print(f"What is {question}? (Type 'xxx' if you want to quit")
    user_input =  int_check("your answer:")

    if user_input == "xxx":
        break



    # todo ask for user ans

    # todo compare with ans, if correct/wrong, store history



    rounds_played += 1

    if mode == "infinite":
        num_rounds += 1



# todo end loop, print something, also result eg: 5/10

# todo ask for hist
if string_checker("Do you want to see Quiz summery?") == "yes":
    print("Your Quiz summery")


