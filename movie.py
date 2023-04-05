# Film Age ratings
age = 0
while age < 1 or age > 117:
    try:
        age = int(input("Enter your age: "))
        if age < 1 or age > 117:
            print("Invalid age. Please enter a number between 1 and 117.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 117.")

if age <= 11:
    print("You can watch U, PG rated movies.")
elif age <= 14:
    print("You can watch U, PG, 12 rated movies.")
elif age <=17:
    print("You can watch U, PG, 12, 15 rated movies.")
else:
    print("You can watch all rated movies.")