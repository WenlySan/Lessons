class BattlePlace:
    def __init__(self, name=str('dd'), x=int(), y=int(), ship=str(), is_ship=False):
        self.name = name
        self.x = x
        self.y = y
        self.ship = ship
        self.hide = False
        self.is_ship = is_ship

    def getinfo(self):
        return self.name, self.x, self.y, self.ship, self.hide, self.is_ship


g = []
sea = '[~]'
miss = '[o]'
ko = '[x]'
ship = '[*]'


for x in range(0, 10):
    for y in range(0, 10):
        g.append(BattlePlace('', x, y, sea, False))




def show_board(gg):
    print(' ', end='')
    for i in range(0, 10):
        print(i, end='  ')
    print()
    for i in gg:
        if gg.index(i) % 10 == 9:
            # print(i.ship, end='3')
            print(i.ship, '-', gg.index(i)//10)
        else:
            print(i.ship, end='')


# g[11].ship = ship
# print(g[11].x, g[11].y)
# for i in g:
#     if g.index(i)
def dot(xy):
    isval = False
    if xy % 10 != 9 and xy > 9 and xy < 90:
        for i in range(0, 3):
            if g[xy - 11 + i].ship == sea and g[xy - 9 + i].ship == sea and g[xy - 1 + i].ship == sea:
                isval = True



            else:
                isval = False
                break
        print('/',xy - 11 + i,'/', xy - 9 + i ,'/',xy - 1 + i)

    if isval == True:
        g[xy].ship = ship
        # print('Yes')
    # else:
        # print('Oh, no')
    return print(isval)
# dot(44)

dot(3)

show_board(g)


