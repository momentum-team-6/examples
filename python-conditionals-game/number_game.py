from random import randint

def choose_number_to_guess():
    number = randint(1, 100)
    print(number)
    return number


def guess_and_check(number):
    guess = int(input('Guess a number between 1 & 100: '))
    if guess > number:
        print("That's too high")
        return False
    if guess < number:
        print("That's too low")
        return False
    print("You're right")
    return True

def play_game():
    game_over = False
    guesses = 0
    number = choose_number_to_guess()
    while not game_over and guesses < 5:
        game_over = guess_and_check(number)
        guesses += 1
        if guesses == 5:
            print("You are out of guesses")
            break


play_game()
