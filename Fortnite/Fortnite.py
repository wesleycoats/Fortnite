#!/bin/python3

from time import *
from random import *
from turtle import *
from math import *
import math
import time

turtle = Turtle()
turtle.speed(0)

player1 = input("Enter Player1's name:")
player2 = input("Enter Player2's name:")

#writes player 1 names and HP
turtle.penup()
turtle.goto(-180,180)
turtle.write(player1)
turtle.goto(-180,170)
turtle.color('#E41A32')
turtle.write('HP')

#write player 2 names and HP
turtle.color('#000000')
turtle.goto(150,180)
turtle.write(player2)
turtle.goto(150,170)
turtle.color('#E41A32')
turtle.write('HP')

#Create HP bars
a1_Health = 100
a1_totalDamage = 0

b1_Health = 100
b1_totalDamage = 0


#player1
turtle.goto(-170,170)
for i in range(2):
  turtle.color('#000000')
  turtle.pendown()
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
turtle.penup()

turtle.goto(-169,169) 
turtle.begin_fill()
for i in range(2):
  turtle.color('#E41A32')
  turtle.pendown()
  turtle.forward(98)
  turtle.right(90)
  turtle.forward(8)
  turtle.right(90) 
turtle.end_fill()  
turtle.penup()

#updates health bars
def updateHealthBars(player, damage):
  global a1_Health
  global b1_Health
  
  global a1_totalDamage
  global b1_totalDamage
  
  #player 1
  if(player == 'player1'):
    a1_totalDamage += damage
    a1_Health = a1_Health - damage
    
    #change = damage
    #98    = 100
    change = (98*a1_totalDamage) / 100
    
    turtle.goto(-71, 169)
    turtle.begin_fill()
    for i in range(2):
      turtle.color('#000000')
      turtle.pendown()
      turtle.backward(change)
      turtle.right(90)
      turtle.forward(8)
      turtle.right(90) 
    turtle.end_fill()  
    turtle.penup()
  
    print(player1 + "'s remaining health is " + str(a1_Health))
    turtle.color(ERROR)
    turtle.goto(0,0)
  
  #player 2
  elif(player == 'player2'):
    b1_totalDamage += damage
    b1_Health = b1_Health - damage
    
    #change = damage
    #98    = 100
    change = (98*b1_totalDamage) / 100
    
    turtle.goto(41, 169)
    turtle.begin_fill()
    for i in range(2):
      turtle.color('#000000')
      turtle.pendown()
      turtle.forward(change)
      turtle.right(90)
      turtle.forward(8)
      turtle.right(90) 
    turtle.end_fill()  
    turtle.penup()
  
    print(player2 + "'s remaining health is " + str(b1_Health))
    turtle.color(ERROR)
    turtle.goto(0,0)

#player2
turtle.goto(140,170)
for i in range(2):
  turtle.color('#000000')
  turtle.pendown()
  turtle.backward(100)
  turtle.left(90)
  turtle.backward(10)
  turtle.left(90)
turtle.penup()

turtle.goto(139,169) 
turtle.begin_fill()
for i in range(2):
  turtle.color('#E41A32')
  turtle.pendown()
  turtle.backward(98)
  turtle.left(90)
  turtle.backward(8)
  turtle.left(90) 
turtle.end_fill()  
turtle.penup()



#draws battlefield
turtle.color('#000000')
turtle.goto(-150,150)
turtle.pendown()
for i in range(4):
  turtle.forward(300)
  turtle.right(90)
turtle.penup()
turtle.goto(-149,149)
turtle.color('#0CD85A')
turtle.pendown()
turtle.begin_fill()
for i in range(4):
  turtle.forward(298)
  turtle.right(90)
turtle.end_fill()
turtle.penup()


#color choices
gray = "#F1EDED"
red = "#EC3B3B"
lightgreen = "#23FF27"
darkgreen = "#3BB83E"
yellow = "#F4FF28"
lightblue = "#84F8FF"
darkblue = "#2889FF"
purple = "#9E28FF"
ERROR = "#0CD85A"

#removes turtle 
turtle.color(ERROR)
turtle.goto(0,0)

colors = [red,lightgreen,darkgreen,yellow,lightblue,darkblue,purple,ERROR]
print('Color options: red, lightgreen, darkgreen, yellow, lightblue, darkblue, purple')

#ask for player colors
a1_Color = input("Player1's color: ")
b1_Color = input("player2's color: ")

#create players
a1 = Turtle()
a1.color(a1_Color)
a1.speed(0)
a1.shape('square')
a1.penup()
b1 = Turtle()
b1.color(b1_Color)
b1.speed(0)
b1.shape('square')
b1.penup()
a1.goto(-135,0)
b1.goto(135,0)
b1.right(180)

#distance between 2 players
distance = math.sqrt((a1.xcor()-b1.xcor())**2 + (a1.ycor()-b1.ycor())**2)

#weapons dictionary
#damage, accuracy, headshot damage, headshot accuracy

weapons = {}
weapons['Double Pump'] = [14, 35/distance, 35, 20/distance]
weapons['Sniper'] = [65, 200/distance, 95, 150/distance ]
weapons['AR'] = [15, 60/distance, 25, 45/distance]
weapons['Sword'] = [90, 10/distance, 300, 5/distance]


#item dictionary
#added health, blocked damage, damage reduction, damage, damage radius
items = {}
items['Mini Shields'] = [25, 0, 0, 0, 0] #adds health, get 4
items['Bulletproof Vest'] = [0, 0, .50, 0, 0,] #reduces bullet damage
items['Handheld Shield'] = [0, 1.0, .10, 0, 0]#block all sword damage, reduces other damage
items['Grenade'] = [0, 0, 0, 15, 60] #splash damage, get 3
items['Invisible Potion'] = [0, 0, 0, 0, 0] #reduces opponent accuracy for 3 turns


#asks player weapons
print("Weapons: Double Pump, Sniper, AR, Sword")
a1_Weapon = input("player1's Weapon:")
b1_Weapon = input("player2's Weapon:")

#asks player items
print("Items: Mini Shields, Bulletproof Vest, Handheld Shield, Grenade, Invisible Potion")
a1_Item = input("player1's Item:")
b1_Item = input("player2's Item:")


#ask user what move they want to make
print('Move Options: (a)-left (s)-down  (d)-right (w)-up')

def useWeapon(player, weapon):
  pass
  
def useItem(player, item):  
  pass

def move(player):
  move = input(player + "'s move:" )
  if player == 'player1':
    if move == 'a':
      a1.backward(50)
    elif move == 'w':
      a1.left(90)
      a1.forward(50)
      a1.right(90)
    elif move == 'd':
      a1.forward(50)
    elif move == 's':
      a1.right(90)
      a1.forward(50)
      a1.left(90)
  elif player == 'player2':
    if move == 'a':
      b1.forward(50)
    elif move == 'w':
      b1.right(90)
      b1.forward(50)
      b1.left(90)
    elif move == 'd':
      b1.backward(50)
    elif move == 's':
      b1.left(90)
      b1.forward(50)
      b1.right(90)


def weaponOrItem(player):
  choice = input(player + ", 1-use weapon, 2-use item, 3-camp:" )
  if player == 'player1':
    if choice == '1':
      useWeapon(player, a1_Weapon)
    elif choice == '2':
      useItem(player, a1_Item)
    elif choice == '3':
      pass
  elif player == 'player2':
    if choice == '1':
      useWeapon(player, b1_Weapon)
    elif choice == '2':
      useItem(player, b1_Item)
    elif choice == '3':
      pass 
    
    
def a1s_turn():
  move('player1')
  weaponOrItem('player1')
  
def b1s_turn():  
  move('player2')
  weaponOrItem('player2')
  


#start game
while True:
  a1s_turn()
  b1s_turn()