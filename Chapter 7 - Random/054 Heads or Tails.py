import random

#054 heads or tails
coinToss = random.choice(["h", "t"])
choice = input("Heads or Trails (h/t)")
while choice != "h" and choice!= "t":
    choice = input("Invalid Answer. Heads or Trails (h/t)")
if choice == coinToss:
    print("You Win")
else:
    print("You Lose")
