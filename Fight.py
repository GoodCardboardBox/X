import random

# คลาสผู้เล่น

class Element:
    #Constructer
    def __init__(self, name, mana, hp):
        self.name=name
        self.mana=mana
        self.hp=hp
        
    # Method
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
    def display_status(self,round_num,hit):
        print(f"<Round: {round_num} ///// Turn: {self.name}>")
        print("-------------------------------------------------------------------------------------")
        print(f"        🔋HP: {Wind.hp}                                         🔋HP: {Water.hp}")
        print(f"        💠 MN: {Wind.mana}                                         💠 MN: {Water.mana}")
        if self.name == Wind.name:
            print(f"                                                         {hit}            ")
        else:
            print(f"                {hit}                                                 ")
        print("           , ,                                                  _ _        ")
        print("        (  •-•)                                                {□~□  }     ")
        print("        /|   |\                                                /|   |\     ")
        print("       🌀|   |🌀                                             🌌 |   | 🌌  ")
        print("         /    \                                                 /    \     ")
        print("-------------------------------------------------------------------------------------")
        print("L Wind attack (Light attack)                                    L Water attack (Light attack)")
        print("N Hurricane attack (Normal attack)                              N Wave attack (Normal attack)")
        print("S Cyclone attack (Strong attack)                                S Flood attack (Strong attack)")
        print("U Tornado attack (Ultimate attack)                              U Tsunami attack (Ultimate attack)")

 
# ฟังก์ชันใช้สกิล

def Light_attackWind(player, opponent):
    dmg = random.randint(15,30)
    opponent.hp -= dmg
    return f"-{dmg}"
def Normal_attackWind(player, opponent):
    player.mana -= 25
    dmg = random.randint(25,50)
    opponent.hp -= dmg
    return f"-{dmg}"
def Strong_attackWind(player, opponent):
    player.mana -= 50
    dmg = random.randint(45,90)
    opponent.hp -= dmg
    return f"-{dmg}"
def Ultimate_attackWind(player, opponent):
    player.mana -= 75
    dmg = random.randint(80,160)
    opponent.hp -= dmg
    return f"-{dmg}"


def Light_attackWater(player, opponent):
    dmg = random.randint(15,30)
    opponent.hp -= dmg
    return f"-{dmg}"
def Normal_attackWater(player, opponent):
    player.mana -= 25
    dmg = random.randint(25,50)
    opponent.hp -= dmg
    return f"-{dmg}"
def Strong_attackWater(player, opponent):
    player.mana -= 50
    dmg = random.randint(45,90)
    opponent.hp -= dmg
    return f"-{dmg}"
def Ultimate_attackWater(player, opponent):
    player.mana -= 75
    dmg = random.randint(80,160)
    opponent.hp -= dmg
    return f"-{dmg}"

def Choose_Skill(Code, player, opponent):
    Code = Code.lower()
    hit = ""
    command = ["l","n","s","u"]
    if Code in command:
        if player.name == "Wind":
            if Code =="l":
                hit = Light_attackWind(player, opponent)
            elif Code =="n" and player.mana >= 25:
                hit = Normal_attackWind(player, opponent)
            elif Code =="s" and player.mana >= 50:
                hit = Strong_attackWind(player, opponent)
            elif Code =="u" and player.mana >= 75:
                hit = Ultimate_attackWind(player, opponent)
            else:
                print("Not enough mana." 
                "\nPlease choose again.")
        else:
            if Code =="l":
                hit = Light_attackWater(player, opponent)
            elif Code =="n" and player.mana >= 25:
                hit = Normal_attackWater(player, opponent)
            elif Code =="s" and player.mana >= 50:
                hit = Strong_attackWater(player, opponent)
            elif Code =="u" and player.mana >= 75:
                hit = Ultimate_attackWater(player, opponent)
            else:
                print("Not enough mana."
                "\nPlease choose again.")
    else:
        print("Wrong skill."
        "\nPlease choose again.")
    return hit
# เทิร์นของผู้เล่น
# เริ่มเกม
# ลูปรอบเกม
# แสดงผลลัพธ์เมื่อเกมจบ
Wind = Element("Wind", 100, 1000)
Water = Element("Water", 100, 1000)
round = int(input("Insert how many round(s)"))
Wind.display_status(1,"")
mana_increase = 0
if round <= 10:
    mana_increase = 20
else:
    mana_increase = 10
for i in range(round):
    atk = ""
    while atk == "":
        Code = input("Choose your skill")
        atk = Choose_Skill(Code, Wind, Water)
    Wind.display_status(i+1,atk)
    atk = ""
    while atk == "":
        Code = input("Choose your skill")
        atk = Choose_Skill(Code, Water, Wind)
    Water.display_status(i+1,atk)
    Wind.mana += mana_increase
    Water.mana += mana_increase
if Wind.hp > Water.hp:
   print("Wind Win!")
elif Water.hp > Wind.hp:
    print("Water Win!")
else:
    print("It's a Tie!")