import random
em={'r':'🪨','p':'📃','s':'✂'}
choices=('r','p','s')
def choice(choices):
    while True:
        ch=input("Rock, Paper, or Scissors? (R/P/S): ").strip().lower()
        if ch not in choices:
            print("Invalid choice!")
            continue
        else:
            return ch

def display(ch,ccp):
    print(f'You chose: {em[ch]}')
    print(f'Computer chose: {em[ccp]}')

def winner(ch,ccp):
    if ch==ccp:
        print("Tie")
    elif ((ch=='r' and ccp=='s') or (ch=='p' and ccp=='r') or (ch=='s' and ccp=='p')) :
        print("You win")
    else:
        print("You lose")
def game():  
    while True:
        ch=choice(choices)
        ccp=random.choice(choices)
        display(ch,ccp)
        winner(ch,ccp)
        c=input('Continue? (Y/N): ').strip().lower()
        if c=='n':
            print("Thanks for playing!")
            break
        elif c=='y':
            print("Let's play again!")
            continue

game() 
    
