from random import shuffle
intial_list = ['x','o','x']
def shuffle_list(intial_list):
    shuffle(intial_list)
    return intial_list
shuffle_list(intial_list)
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a correct number 0/1/2:")
    return int(guess)
player_guess = player_guess()
def check_guess(intial_list,guess):
    if intial_list[guess] =='o':
        print("correct!")
    else:
        print("better luck next time!!")
check_guess(intial_list,player_guess)  

        




