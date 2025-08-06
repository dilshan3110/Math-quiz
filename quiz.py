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

def int_check(question, low=None, high=None, exit_code=None):
    """Checks integers if it is above low or below high and exit code."""
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# stored variables
valid_ops = ["+", "-", "*", "/"]
game_history = []
rounds_played = 0
correct_count = 0
incorrect_count = 0
mode = "regular"

# Main Routine
print("Welcome to Math Quiz\n")

want_instructions = string_checker("Do you want to see instructions? ")
if want_instructions == "yes":
    instructions()

num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ", low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 1

# Game loop starts here
while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    # printing operations into questions
    operation = random.choice(valid_ops)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = ""
    if operation == '-': # if a problem is subtraction, make the first number bigger than the seconds it doesn't become a negative.
        if a < b:
            a, b = b, a
        answer = a - b
    if operation == '+':
        answer = a + b
    if operation == '/': # if question/problem is division, make the first number amount to A times B and then answer = a
        answer = a
        a = a * b
    if operation == '*':
        answer = a * b

    user_answer = int_check(f"{a} {operation} {b} = ", low=0, exit_code="xxx")

    if user_answer == "xxx":
        break

    if user_answer == answer:
        feedback = "You are CORRECT"
        correct_count += 1
    else:
        feedback = "You are WRONG"

    # print infinite mode
    if mode == "infinite":
        print(feedback, f"Answer was {answer}")
        num_rounds += 1

    # print question answer after problem is solved and shows if answer is correct or incorrect.
    quiz_history = f"Question {rounds_played + 1}: {feedback}. Answer is {answer}"
    game_history.append(quiz_history)

    rounds_played += 1

# print quiz summary
if rounds_played > 0:
    print("\nResults")
    print()
    if mode == "infinite":
        num_rounds -= 1
    print(f"You got {correct_count}/{num_rounds} correct 🎊")
    print()

    if mode == "regular":
        see_results = string_checker("Do you want to see quiz results / answers?")
        if see_results == "yes":
            for something in game_history:
                print(something)

else: # print message if you exit code without answering questions
    print("\nYou did not answer any questions and quit")