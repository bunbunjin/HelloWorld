class Car:
    color = ''
    name = ''
    def __init__(self, color, name):
        self.color = color
        self.name = name


    def cars(self):
        print(f'車の名前は{self.name}色は{self.color}です。')



c = Car('赤', 'ヴェルファイア')
c.cars()