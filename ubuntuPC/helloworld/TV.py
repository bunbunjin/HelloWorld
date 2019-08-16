class Tv:
    name = ''
    number = 0

    def __init__(self, name, numeber):
        self.name = name
        self.number = numeber


    def aaa(self):
        print(f'番組名{self.name}、チャンネル{self.number}です。')


channel = input('見たテレビ番組を入力してください。')
channel_n = input('番組のチャンネルを入力してください。')
channel_number = int(channel_n)

t = Tv(channel, channel_number)
t.aaa()
