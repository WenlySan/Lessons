from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


game_place = [[0, 1, 2],   # Можно удалить,ноо пусть пока что будет, соседи спросят, а у тебя есть
              [0,1,2],
              [0,1,2]]
win = [None for i in range(1, 10)]
lot_x = ['X' for i in range(0, 3)]
lot_o = ['O' for i in range(0, 3)]
xoro = True #орпеделяет ход игрока Х или О
# print(lot_o)

def open_info(player):  #Информация победителя
    showinfo(title="Информация", message=f"Победил {player}")

class CheckButton: # Кнопки игровое поле
    def __init__(self, master, title,r,c,id_var):
        self.var = IntVar(value=0)
        self.var.set(id_var)
        self.title = title
        self.cb = Button(
            master, text=self.title,
            width=10,height=5,command=self.xo)
        self.cb.grid(row=r, column=c)
        # print(self.var.get(), 'ads', self)

    def xo(self):
        # print(self,'tttttttttt addasd',self.var.get())
        global xoro,win
        print(win)
        if xoro and ((win[self.var.get()]) == None):
            self.cb.configure(text="X")
            xoro = False
            win[self.var.get()] = "X"
            print(is_win(win,lot_x))
            if (is_win(win,lot_x)):
                click_button()
                open_info('X')


        elif not(xoro) and ((win[self.var.get()]) == None):
            self.cb.configure(text="O")
            xoro = True
            win[self.var.get()] = "O"
            print(is_win(win, lot_o))
            if (is_win(win,lot_o)):
                click_button()
                open_info('O')
        print(win)


def click_button(): # Кнопка сброса игры. Обнуляет поле
    global win,xoro
    # value = clicks.get()    # получаем значение
    # clicks.set(value + 1)
    print(clicks)

    for u in checks:
        u.cb.configure(text="")
        # print(u.var.get(),'lll')
    win = [None for i in range(1, 10)]
    xoro = True

def is_win(w,lot): # Проверка победителя
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
    elif [w[1],w[4],w[7]] == lot:
        return True
    elif [w[0],w[4],w[8]] == lot:
        return True
    elif [w[6],w[4],w[2]] == lot:
        return True
    else:

        return False


root = Tk()
root.geometry("500x500")
# tt44 = ' ddd'
f1 = Frame()
f1.pack(expand=True)#(anchor = "center",padx=1, pady=20)

checks = []
id_var = 0
clicks = IntVar(value=0)

for r in range (len(game_place)):
    for c in range (len(game_place)):
        print(r,c)

        checks.append(CheckButton(f1, '', r, c,id_var))
        id_var += 1

# btn = (ttk.Button(f1,text="Click me", command=ppp)
# btn = (ttk.Button(f1,text= "Старт", command=click_button)) #textvariable=clicks
# btn.grid(row=5, column=1)
btn2 = Button(root, text="Старт", command=click_button )
btn2.place(x=125, y=400,width=250, height=80)


root.mainloop()