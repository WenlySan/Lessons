w = [str(i) for i in range(1,10)]
print(w)
x = "X"
w[1] = x
w[0] = x
w[8] = x
print(w)
lot = ['X','X','X']

print(w[2] == None, w[1] == None )


# if (123 == 'X' or 'O') or (456 == 'X' or 'O') or (789 == 'X' or 'O') or (147 == 'X' or 'O') or (258 == 'X' or 'O') or (369 == 'X' or 'O') or (159 == 'X' or 'O') or (753 == 'X' or 'O'):
#     print(w)
#
# for i in range(0,8):
#     win[i]
# print(w[0:3])
# print(w[3:6])
# print(w[6:9])
# print(w[0:9:3])
# print(w[2:9:3])
# print([w[1],w[5],w[8]])
# print([w[0],w[4],w[8]])
# print([w[6],w[4],w[2]])

def is_win(w,lot):
    if w[0:3] == lot:
        return True
    elif w[3:6] == lot:
        return True
    elif w[6:9] == lot:
        return True
    elif w[0:9:3] == lot:
        return True
    elif w[2:9:3] == lot:
        return True
    elif [w[1],w[5],w[8]] == lot:
        return True
    elif [w[0],w[4],w[8]] == lot:
        return True
    elif [w[6],w[4],w[2]] == lot:
        return True
    else:

        return False
print(is_win(w,lot))











# game_place = [{None,1,2},
#               {0,1,2},
#               {0,1,2}]
# win = [str(i) for i in range(0,3)]
# print(type(win))
# win = [win for i in range(0,3)]
# print(win,type(win))
#
# # win[1[1]] = 'r'
# print(type(game_place[1]))
#
# # for i in win:
#     for y in i:
#         print(y)



