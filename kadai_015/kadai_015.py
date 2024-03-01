class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(f"名前：{self.name}")
        print(f"年齢：{self.age}歳")

profile = Human("侍太郎", 36)

profile.printinfo()