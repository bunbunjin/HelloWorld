class Human:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def greet(self):
        print(f'私は{self.name}といいます。年齢は{self.age}歳です。')


h = Human('kajie', 16)
h.greet()

