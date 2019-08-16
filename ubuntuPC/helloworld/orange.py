class Orange:
    kind = ''
    number = 0

    def __init__(self, kind, number):
        self.kind = kind
        self.number = number

    def last(self):
        print(f'{self.kind}色、{self.number}個')

orange_color = input('オレンジの色')



orange_number = input('オレンジの個数')
orange_int = int(orange_number)

o = Orange(orange_color, orange_number)
o.last()

