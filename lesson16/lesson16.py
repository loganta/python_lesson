import random

number = random.randint(1,99)
guesses = 0

while guesses < 5:
	guess = int(input("Enter an integer from 1 to 99: "))
	guesses += 1
	print ("This is your %d guess" %guesses)


	if guess < number:
		print ("guess is low")

	elif guess > number:
		print ("guess is high")

	elif guess == number:
		break

if guess == number:
	guesses = str(guesses)
	print ("You guess it in:", guesses + "guesses")

if guess != number:
	number = str(number)
	print ("The secret number was", number)