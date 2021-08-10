num = 100
guesses = 5
while(True):
    a = int(input("Enter a number: "))
    if guesses == 0:
        print("You have no guesses left")
        break
    if a == num:
        print("You have Guessed Right")
        break
    elif a > num:
        print("Try a smaller number")
        guesses = guesses - 1
        print("You have ", guesses, "guesses left")
        continue
    elif a < num:
        print("Try a larger number")
        guesses = guesses - 1
        print("You have ", guesses, "guesses left")
        continue