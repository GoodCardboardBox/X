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
# ฟังก์ชันใช้สกิล
# เทิร์นของผู้เล่น
# เริ่มเกม
# ลูปรอบเกม
# แสดงผลลัพธ์เมื่อเกมจบ
O2 = Element("Oxygen", 100, 1000)
H2O = Element("Carbon Dioxide", 50, 2000)
print(O2.is_alive())