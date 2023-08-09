import random # to generate random numbers(inbuit)
def num_guess():
    attempt_limit=15
    rounds=2
    score=0
    
    player=input("hello !! ,what's your name:")
    print("welcome to guessing number game!!!\n"+player+'guess a number between 1 and 100')
    
    for round_num in range(1,rounds+1):
        tar_num=random.randint(1,100)
        for attempt in range(1,attempt_limit +1):
            guess_num=int(input(f'Attempt {attempt} :enter your guess:'))
            
            if guess_num==tar_num:
                print("Congratulations!! You guessed the correct number!")
                round_score=attempt_limit -attempt+1
                score+=round_score
                break
            elif guess_num<tar_num:
                print("Your guess is too low.Try again")
            else:
                print("Your guess is too high.Try again")
        else:
            print(f'\nOops. Out of attempts! {tar_num} is the correct number')
    print(f"\nGame over.'your total score is{score}")
if __name__=="__main__":
    num_guess()        
            
            
        
