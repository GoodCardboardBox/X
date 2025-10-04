# x=input("What's your name?")
# print("Hello1")
# print (x)
# print(int(11*2.5))
# print(float(4*2))
# print(int(5/2))
# print(int(6/3))

# print(str("a"))
# print(str("b"))
# print (str(a)+str(b))

# a="100"
# b="10"

# print(int(a)+int(b))
# a="999"
# b=1
# c=1010
# d="abc"
# x=int(a)+b
# print(str(c)+d+str(int(a)+b))
# a = input ('Please enter your name: ')
# print ('My name is ', a)
# a = int(input ('Please enter your year of birth: '))
# print ('I am ' , 2024 - a)






# R = int(input("Enter radius of the circle"))
# import math 
# c = 2*math.pi*R
# a = math.pi*R**2
# C = ("The circle's circumference is:")
# A = ("The circle's area is:")
# print(F"The circle's circumference is:{c:.2F}")
# print(F"The circle's area is:{a:.2F}")


# import math
# print("Welcome to Pythagoras-Theorem Calculation!")

# a = int(input("intput a value:"))
# b = int(input("intput b value:")) 
# c = math.sqrt(a**2 + b**2)
# print(f"a = {a} , b = {b} Answer c is {c:.3f}")

# a=input().split()
# a[1]=int(a[1])
# a[3]=int(a[3])
# print(a[1]+a[3])

# a=input("Input Your numbers:").split()
# a=[int(x) for x in a]
# abc=a[0]+a[len(a)-1]
# print(f"The result of the first number plus the last number is {a[0]} + {a[len(a)-1]} = {abc}")
# a.append(abc)
# print(f"Your list is {a}")
# cat = {"name" : 'สามสี', "sound": 'meow', "Legs": 4 , "like" : "fish"}
# cat["name"]= "Jhon"
# cat["sound"]="bong"
# cat["like"]="meat"
# print(f"ฉํนมีแมวชื่อ{cat["name"]} มันร้อง {cat["sound"]} มี {cat["Legs"]} ขา ชอบกิน {cat["like"]}")
# person1 = {"name" : "Atom", "age" : 13, "height" : 155, "weight" : 50, "gender" : "female"}
# index,value = input("input index and value :").split()
# person1[index] = value
# print (person1)
# "John":  ["male",180.5,80],
#     "Jane":  ["female",176,60.5],
#     "Steve": ["male",187.5,82]

# Heroes =[
#     {"name" : "ไอ้ปื๊ด", "type" : "Melee", "hp" : 165, "atk" : 20},
#     {"name" : "น้องไนซ์",  "type" : "Magician", "hp" : 140, "atk" : 25},
#     {"name" : "พี่หน่วง",  "type" : "Range", "hp" : 120, "atk" : 30},
#     {"name" : "เก่ง พลังช้าง",  "type" : "Defence", "hp" : 300, "atk" : 10}]
# index, name, type, hp, atk = input("Edit Your Heroes").split()
# Heroes[int(index)]["name"]= name
# Heroes[int(index)]["type"]= type
# Heroes[int(index)]["hp"]= int(hp)
# Heroes[int(index)]["atk"]= int(atk)
# print(Heroes)

# buy = input("Do you want to buy : ")
# if buy == "yes" :
#      print("rich")
# else :
#     print("save money")
# print("keep working")

# import random
# money = 100
# lottery = (input(" Do you want to buy lottery? positive or negative? "))
# if lottery == "positive" :
#     number = int(input("please pick the number 1-15"))
#     win = (random.randrange(1,15))
#     print(win)
#     if number == win :
#         money += 100000
#         print (f"I have {money}")
#     else :
#         print (f"I have {money}")
# else :
#     print("I'm gonna save money")
#     print (f"I have {money}")

# x = int(input("Your score is"))
# if  x>=90 and x<=100 :
#     print("A+")
# elif  x>=85 and x<=89 :
#     print("A")
# elif  x>=75 and x<=84 :
#     print("B+")
# elif  x>=65 and x<=74 :
#     print("B")
# elif  x>=55 and x<=64 :
#     print("C+")
# elif  x>=45 and x<=54 :
#     print("C")
# elif  x>=35 and x<=44 :
#     print("D+")
# elif  x>=25 and x<=34 :
#     print("D")
# elif  x>=0  and x<=24 :
#     print("F")

# myUser = {"username": "admin", "password": "admin123"}
# username, password = (input("input your username and password").split())
# if username =="admin" and password =="admin123":
#     print("Log in success")
# elif username !="admin" and password !="admin123":
#     print("incorrect password and username")
# elif username !="admin":
#     print("incorrect username")
# elif password !="admin123":
#     print("incorrect password")

# import random
# Answer = random.randint(1, 20)
# choose_Num = 0
# while Answer != choose_Num :
#     choose_Num = int(input("Your guess is"))
#     if choose_Num < Answer :
#         print("higher")
#     elif choose_Num > Answer :
#         print("lower")
#     else  :
#         print("You guess it right")

# hello = input("input any word")
# x = int(input("insert loop"))
# n = 1
# while n <= x:
#    print(hello)
#    n += 1

# WOW = int(input("insert number of num"))
# KEEP = 0
# for i in range (WOW):
#     WHAT = int(input("insert num"))
#     KEEP = KEEP+WHAT
# print(KEEP)

# bye = input("input any word1")
# hello = input("input any word2")
# x = int(input("insert loop"))
# for i in range (x):
#    if  i % 2==0:
#     print(hello)
#    else:
#     print(bye)

# import random 
# Play = (input("Do you want to play Rock, Paper, Scissor? Yes or No?"))
# if Play == "Yes": 
#     Scores_Player = 0
#     Scores_Bot = 0
#     for i in range (3):
#      print("Round i")
#      Player = int(input("Rock(1) Paper(2) Scissor(3)"))
#      Bot = random.randint(1,3)
#      print (Bot)
#      if Player == Bot: print ("draw")
#      elif Player == 1 and Bot == 2: 
#         print ("BOT SCORED")
#         Scores_Bot += 1
#      elif Player == 2 and Bot == 3: 
#         print ("BOT SCORED")
#         Scores_Bot += 1
#      elif Player == 3 and Bot == 1: 
#         print ("BOT SCORED")
#         Scores_Bot += 1 
#      elif Player == 2 and Bot == 1: 
#         print ("PLAYER SCORED")
#         Scores_Player += 1    
#      elif Player == 3 and Bot == 2: 
#         print ("PLAYER SCORED")
#         Scores_Player += 1
#      elif Player == 1 and Bot == 3: 
#         print ("PLAYER SCORED")
#         Scores_Player += 1
#      print (f"Player's scores = {Scores_Player}")
#      print (f"Bot's scores = {Scores_Bot}")
#     if Scores_Bot > Scores_Player:
#       print ("BOT WINS!")
#     elif Scores_Bot < Scores_Player:
#       print ("PLAYER WINS!")
#     elif Scores_Bot == Scores_Player:
#       print ("DRAW!")
# else:
#    print("Bye bye")

# list_Movie = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King", 
#               "Inception", "The Godfather: Part II", "The Dark Knight Rises", "Interstellar", "The Avengers"]
# for Ticket in list_Movie:
#     print(Ticket)
# Answer = (input("Do you want to watch or no?"))
# if Answer == ("no"):
#     print("THEN GET THE HELL OUT OF THE THEATER")
# else:
#     Ticket = int(input("What do you want to watch?(1-10)"))
#     print(f"Have fun watching {list_Movie[Ticket-1]}!")
# list = int(input("How many to do list do you need?"))

# To_do = []
# for i in range(list):
#         New_to_do = input("What kind of list you going to do?")
#         To_do.append(New_to_do)
# print("Here's your to do list!")
# print(To_do)
# for i in range(list):
#     print(f"{i+1} . {To_do[i]}")



# for i in range(5):
#     for j in range(5):
#         if i==3:
#             print("-",end=" ")
            
#         elif i==1:
#             print("-",end=" ")
#         elif j==3:
#             print("|",end=" ")
#         elif j==1:
#             print("|",end=" ") 
#         elif i==1:
#             print("-",end=" ") 
#         elif i==0:
#             print("X",end=" ")
#         elif i==2:
#             print("X",end=" ")
#         elif i==4:
#             print("X",end=" ")
#         else:
#             print("-",end=" ")
    
#     print()
# round = 1
# while True:
#     print("------------------------------------------------------")
#     print()
#     print(f"round: {round}")
#     print()

#     for i in range(5):
#         for j in range(5):
#             if i%2==0 :
#                 if j%2==0:
#                     print(" ", end=" ") #ช่อง X O
#                 else:
#                     print("|", end=" ")
#             else:
#                 print("-", end=" ")
#         print()
#     if round%2==0:
#         ans=input("X: ")
#     else:
#         ans=input("O: ")
#     round=1+round


# xo=[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],
#  [" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]



# while True:
#     print("_ _ _ _ _ _ _ _ _ _ _ _ ")
#     for i in range(10):
#         for j in range(10):
#             if j == 0:
#                 print("|", end=" ")
              
#             print(xo[i][j], end=" ")
#             if j == 9:
#                 print("|", end=" ") 
#         print()
#     print("_ _ _ _ _ _ _ _ _ _ _ _ ")   
#     po = input("i :")
#     op = input("j :")
#     googa = input("character")
#     xo[int(po)][int(op)]=googa
#     (po,op)
#     print(po)
#     print(op)
#     print(int(po))
#     print(int(op))



# xo=[[" "," "," ",],[" "," "," ",],[" "," "," ",]]

# count=0
# full=True
# while True:
    
#     for i in range(3):
#         print("_ _ _ _ _ _ _")    
#         for j in range(3):
            
#             print("|", end=" ") #front line
              
#             print(xo[i][j], end=" ")
#             if j == 2:
#                 print("|", end=" ") #back line
#         print()
#     print("_ _ _ _ _ _ _")   
 
#     po = input("i :")
#     op = input("j :")
    
#     googa = "X"
#     if count %2 == 0: 
#         googa = "X"
#     else:
#         googa = "O"
#     if xo[int(po)][int(op)]!=" ":
#         print("Unstackable")
#         continue
        
#     xo[int(po)][int(op)]=googa

#     if xo[0][0]==googa and xo[0][1]==googa and xo[0][2]==googa:
#         break
#     elif xo[1][0]==googa and xo[1][1]==googa and xo[1][2]==googa:
#         break
#     elif xo[2][0]==googa and xo[2][1]==googa and xo[2][2]==googa:
#         break
#     elif xo[0][0]==googa and xo[1][0]==googa and xo[2][0]==googa:
#         break
#     elif xo[0][1]==googa and xo[1][1]==googa and xo[2][1]==googa:
#         break
#     elif xo[0][2]==googa and xo[1][2]==googa and xo[2][2]==googa:
#         break
#     elif xo[0][0]==googa and xo[1][1]==googa and xo[2][2]==googa:
#         break
#     elif xo[0][2]==googa and xo[1][1]==googa and xo[2][0]==googa:
#         break
#     full = True 
#     for i in range (3):
#         for j in range (3):
#             if xo [i][j] ==" ":
#                 full = False
#     if full:
#         break
#     count = count + 1
# for i in range(3):
#         print("_ _ _ _ _ _ _")    
#         for j in range(3):
            
#             print("|", end=" ") #front line
              
#             print(xo[i][j], end=" ")
#             if j == 2:
#                 print("|", end=" ") #back line
#         print()
# print("_ _ _ _ _ _ _")
# if full:
#     print("Draw!!")
# else:
#     print(f"{googa} Win!!")
# input
# length = int(input())
# width = int(input())
# for i in range(length):
#     for j in range(width):
#         if i==0:
#             print("-",end=" ")
#         elif i==length-1:
#             print("-",end=" ")
#         elif j==0:
#             print("|",end=" ")
#         elif j==width-1:
#             print("|",end=" ") 
#         else:
#             print("*",end=" ")
#     print() 
# width = int(input("Enter the width: "))
# height = int(input("Enter the height: "))

# for i in range(height):
#     for j in range(width):
#         if i == 0 or i == height - 1:
#             print("-", end=" ")
#         elif j == 0 or j == width - 1:
#             print("|", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# map=[]


# print("- " * (width+2))
# for i in range(height):
#     map.append([])
#     for j in range(width):
#         if j == 0 :
#             print("|", end=" ")
#         print("*", end=" ")
#         map[i].append("*")
#         if j == width - 1:
#             print("|", end=" ")
#     print()
# print("- " * (width+2))

# print("<-------------------------------------->")


# while True:
#   pos = input("Enter the position: ").split(" ")
#   if pos[0] == "exit":
#     break
#   pos = [int(pos[0]), int(pos[1])]
#   map[pos[0]][pos[1]] = "X"

#   print("- " * (width+2))
#   for i in range(height):
#       for j in range(width):
#           if j == 0 :
#               print("|", end=" ")
#           print(map[i][j], end=" ")
#           if j == width - 1:
#               print("|", end=" ")
#       print()
#   print("- " * (width+2))
# Tralala = []
# for i in range(5):
#     Tralalero = int(input(i+1))
#     Tralala.append(Tralalero)
#     print(Tralala)
# print(max(Tralala))

# Trippi = []
# for i in range(5):
#     Troppi = int(input("num"))
#     Trippi.append(Troppi)
# print(Trippi)
# Patapim = sum(Trippi)
# print(Patapim)

# Student = {}
# for i in range(3):
#     Bombardino = input("name")
#     Crocodilo  = int(input("score"))
#     Student[Bombardino] = Crocodilo
# print(Student)
# max = 0
# for k in Student:
#     if Student[k] > max:
#         max = Student[k]
# print(max)

# fav_numbers = [42, 77, 35, 90, 12, 55, 63, 25, 10, 80]
# Cappuccino = 0 
# for k in fav_numbers:
#     print(k)
#     if k > 50:
#         Cappuccino += 1
# print(f"numbers that are more than 50: {Cappuccino}")

# fav_numbers = [42, 75, 33, 80, 95, 49, 50, 66, 70, 30]
# Capuccina = 0 
# for k in fav_numbers:
#     print(k)
#     if k >= 50:
#         Cappuccina += 1
# print(f"numbers that are more than 50: {Cappuccina}")

# students = students = [
#     {"name": "Anna", "height": 160.0},
#     {"name": "Ben", "height": 165.2},
#     {"name": "Cara", "height": 158.5},
#     {"name": "David", "height": 170.3},
#     {"name": "Steve", "height": 177.5}
# ]
# Assasino = 0 
# Capuccino =" "
# for k in students:
#     print(k)
#     if k["height"] > Assasino:
#         Capuccino =k["name"]
#         Assasino = k["height"]
# print(f"Student that is the highest: {Capuccino} {Assasino}")

# Players ={
#     "Arin": ["Warrior", 150, 75],
#     "Luna": ["Mage", 120, 90],
#     "Kira": ["Assassin", 100, 95],
#     "Gorn": ["Warrior", 180, 80],
#     "Zane": ["Mage", 130, 88]
# }
# Chimpanzini = 0
# Bananini =" "
# Frulli = 0
# for i in Players:
#     print(f"{i} the {Players[i][0]} has {Players[i][1]} HP and {Players[i][2]} Power.")
#     if Players[i][2] > Chimpanzini:
#         Bananini = i
#         Chimpanzini = Players[i][2]
#     Frulli += Players[i][1]
# Average = Frulli / len(Players)
# print(f"Player that is the Strongest: {Bananini} {Chimpanzini}")
# print(f"Average HP of all players is {Average}")

# function แบบไม่มี return
# def EvenOrOdd(x):
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# EvenOrOdd(15)
# function แบบมี return
# def XplusY(x,y):
#     return x+y    
# print(XplusY(2,3))

# def JK(wow,how):
#     return wow * how
# print(JK(4,5))

# def OJ(how, wow, lao):
#    hongkong = 0
#    if wow == "+":

#     hongkong = how + lao
#    else:
#     hongkong = how - lao
#    return hongkong
# print(OJ(4,"+",5))

# def Poop(Homeless):
#     Normal = sum(Homeless)
#     return Normal
# Rich = []
# for i in range(3):
#     Broke = int(input("num"))
#     Rich.append(Broke)
# print(Rich)
# print(Poop(Rich))

# def OJ(lao):
#     if lao < 20:
#         print("It's so frickin' cold!")
#     else:
#         print("It's so frickin' hot!")
# hongkong = int(input("Enter temperature"))
# OJ(hongkong)

# def drawLine(x):
#     for i in range(x):
#             print("*",end = "")
# def drawTriangle(y):
#       for i in range(y):
#         drawLine(i)
#         print()
# drawTriangle(5)

# def sumAndAvg(bla, ble, blo):
#     bruh = bla + ble + blo
#     brah = bruh / 3
#     return bruh, brah
# total, mean = sumAndAvg(10, 10, 10)
# print(f"Sum: {total}, Average: {mean:.2f}")

# Student = {
#     "John Wick":{"Math":50, "Science": 85,},
#     "Jackie Chan":{"Figthing":100, "Math": 25}
#     }
# def add_student(name):
# def add_subject(name,subject,score)

# import turtle as t
# t.width(5)
# t.color("#000000")
# def ring(lap):
#  for _ in range(lap):
#     t.forward(100)
#     t.left(360 / lap)
# ring(5)
# t.penup()
# t.goto(-80, 150)
# t.color('green')
# message = "Welcome to Python and Turtle!"
# t.write(message, font=("Arial", 20, "normal"))
# print(message)  
# t.done()

# import turtle as t
# t.color("#ff0000")
# def drawTriangle(length):
#  for _ in range(3):
#     t.forward(length)
#     t.left(360 / 3)
# def drawSquare(length):
#  for _ in range(4):
#     t.forward(length)
#     t.left(360 / 4)
# def drawHouse():
#     drawSquare(50)
#     t.left(90)
#     t.forward(50)
#     t.right(90)
#     drawTriangle(50)
# t.speed(1000)
# t.penup()
# t.goto(-200,0)
# t.pendown()
# drawHouse()
# t.right(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.penup()
# t.forward(25)
# t.pendown()
# drawHouse()
# t.right(90)
# t.forward(50)
# t.left(90)
# t.penup()
# t.forward(75)
# t.pendown()
# drawHouse()
# t.right(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.penup()
# t.forward(25)
# t.pendown()
# drawHouse()
# t.right(90)
# t.forward(50)
# t.left(90)
# t.penup()
# t.forward(75)
# t.pendown()
# drawHouse()
# def drawSoi(space):
# def drawPhase(space):
# def drawVillage():
# t.done()

# import random
# P1 = 0
# P2 = 0
# turn = 1
# round = 1
# game_over = False
# winner = 0
# def reset_game():
#     global P1, P2, turn, round, game_over, winner
#     P1 = 0
#     P2 = 0
#     turn = 1
#     round = 1
#     game_over = False
#     winner = 0
# def random_dice():
#     return random.randint(1, 6)
# def calculate_point():
#     global P1, P2, turn
#     if turn == 1:
#         x= input("Player1 press enter to roll the dice")
#         P1 = P1 + random_dice()
#     else:
#         x= input("Player2 press enter to roll the dice")
#         P2 = P2 + random_dice()
# def display_point():
#     global P1, P2, turn
#     if turn == 1: 
#         print(f"Player1 rolled {P1}")
#     else: 
#         print(f"Player2 rolled {P2}")
#     take_turn()
# def take_turn():
#     global turn
#     if turn == 1:
#         turn = 2
#     else:
#         turn = 1

# def display_winner():
#     global P1, P2, game_over
#     if P1 >= 100:
#         print("Player1 win!")
#         game_over = True
#     if P2 >= 100:
#         print("Player2 win!")
#         game_over = True
# while not game_over:
#     calculate_point()
#     display_point()
#     display_winner()

# for i in range(0, 10):
#     print("hello Atom")

class monster:
    #Constructer
    def __init__(self, name, colour):
        self.name=name
        self.colour=colour
        self.HP=500
        self.DMG=50
    # Method
    def Roar(self):
        print("GRR")

# Create an instance of the car class and call the accelerate1 method
monster1= monster("Glub", "Green")
monster1.Roar()