import random

while True:
 n=input("enter y or no: ").lower()

 if n=='y':
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'({die1},{die2})')
 elif n=='n':
    print("thanks for playing")
    break
 else:
    print("Invalid choice")
    break
    
