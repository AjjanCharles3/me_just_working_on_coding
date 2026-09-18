
name=(input("whats your name? "))
age=int(input( " So how old were you again? "))
print("name:", name)
print("age:", age)
import random
dice = random.randint(1, 20)
print("You rolled a", dice)
situation = "You rolled a natural 1!" if dice == 1 else "You rolled a critical hit!" if dice == 20 else "You rolled a regular roll."
print(situation)
Weapon =("long Sword", +2)
attack_roll = random.randint(1,20) + Weapon[1]
print("You rolled a", attack_roll, "with your", Weapon[0])