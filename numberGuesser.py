import random

top_of_range=input('type in a no.: ')
if top_of_range.isdigit():
    top_of_range=int (top_of_range)

    if top_of_range <= 0:
        print('Please type in a no greater than 0 next time!')
        quit()
else:
    print('Enter a number next time!')
    quit()

random_number = random.randint(0,top_of_range)
#print(random_number)
guesses=0
while True:
    guesses+=1
    user_guess=input('Make a guess?')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please type in  no.')
        continue
    if user_guess==random_number:
        print('You got it,',guesses,'guesses')
        break
    elif user_guess > random_number:
            print('You are above the number!')
    else:
            print('You are below the number!')
