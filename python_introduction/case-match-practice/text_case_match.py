#input value
# Input values
voters_card = input("Do you have a voter's card (yes, no)? ").lower()

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number. Age must be a number.")
    exit()

# Match-case logic
match age:
    case x if x >= 18 and voters_card == "yes":
        print("You are eligible to vote and have a voter's card.")
    case x if x >= 18 and voters_card == "no":
        print("You are eligible to vote but do not have a voter's card.")
    case x if x < 18 and voters_card == "yes":
        print("You are not eligible to vote but you have a voter's card.")
    case _:
        print("You are not yet eligible to vote.")
