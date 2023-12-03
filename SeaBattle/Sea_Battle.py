

# battle_place = {}
# battle_place_test = [_ for _ in range(1,11)]
# bt_p =[chr(i) for i in range(1072, 1072+9)]
# bt_p.append(chr(1082))
sheep = [1,1,1,1,2,2,2,3,3,4]

player = []
def creat_place():
    battle_place = {}
    for _ in range(0,10):
        for i in range(0, 10):
            battle_place[ int(str(_) +str(i))] = '[ ]'
    return battle_place
# for key in bt_p:
#     for value in battle_place_test:
#         #print(str(key) + str(value), end = ' ')
#         battle_place[str(key) + str(value)] = '[ ]'
#     #print()

# print(ord('а'), *bt_p)
#
# print(battle_place.keys())
def view_place(place):
    count = 1
    print(' ',end=' ')
    for i in range(0,10):
        print('',i, end='  ')
    print('')
    for i,_ in place.items():
        if count == 1:
            print(i//10,end=' ')
        if count == 10:
            count = 1
            print((_),sep='')

        else:
            print((_),end=' ')
            count += 1


battle_place = creat_place()
battle_place[22] = '[*]'
view_place(battle_place)

print(battle_place.get(22))
view_place(battle_place)

if battle_place.get(22) == '[*]':
    print('Иди от сюда')

# if battle_place['22'] ==
# wtf = battle_place['22']
