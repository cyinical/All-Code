import random
import time
from time import sleep

#Base hitpoints
enemyHitPoints = 10
playerHitPoints = 20

#Defence
enemyDefence = 5
playerDefence = 10

print("You awake with a pounding headache, you stand but are slightly nauseous.")
sleep(3)
print("You eye a creature and deside it's a good way of waking up if you hit it on the head a couple of times before breakfast")
sleep(3)
print("*Your encounter starts!*")

#Attack
def enemyAttackDamage():
    enemyDamage = random.randint(1,3)
def playerAttackDamage():
    playerDamage = random.randint(1,5)

#Chance to Hit
def enemyChance():
    enemyChanceToHit = random.randint(1,10)
    if playerDefence == 0:
        print('It broke your armour and hit you directly')
