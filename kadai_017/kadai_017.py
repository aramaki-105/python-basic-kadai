class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"名前：{self.name} 年齢：{self.age}歳 大人です。")
        else:
            print(f"名前：{self.name} 年齢：{self.age}歳 大人ではありません。")

ashida = Human("芦田 愛菜", 19)
kitagawa = Human("北川 景子", 37)
hirose = Human("広瀬 すず", 25)
terada = Human("寺田 心", 15)

human_list = [ashida, kitagawa, hirose, terada]

for person in human_list:
    person.check_adult()