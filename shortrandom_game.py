import random

def generator(guess, answer):
    if 0 < int(guess) < 11:
        if guess == answer:
            print('you are a genius')
            return True
    else: 
        print('Hey! I said 1~10')
        return False

if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if(generator(guess, answer)):
                break
        except ValueError:
            print('ValueError: Enter a number')
            continue