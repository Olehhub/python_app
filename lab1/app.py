from json.tool import main
from tkinter import *
from tkinter import messagebox
from functions import *
from random import sample

main_set = []
setA = set
setB = set
setC = set
setU = set


# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------
root = Tk()
root.title("New Application by Oleh Bielov")
root.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
root.geometry("400x500")

# Exit Button
exit_button = Button(root, text="exit", command=root.quit)
exit_button.place(x=360, y=370)

#Entry viget
rbA = Entry(root, borderwidth = 5, state = NORMAL)
rbA.place(x = 140, y = 230)
rbB = Entry(root, borderwidth = 5, state = NORMAL)
rbB.place(x = 140, y = 290)
rbC = Entry(root, borderwidth = 5, state = NORMAL)
rbC.place(x = 140, y = 350)
rbU = Entry(root, borderwidth = 5, state = NORMAL)
rbU.place(x = 140, y = 410)


setpower = Entry(root, borderwidth = 5, state = NORMAL)
setpower.place(x = 140, y = 140)


#Some Labels
txt_label = Label(root, text = "Виберіть мод")
txt_label.place(x = 165, y = 20)

A_label = Label(root, text = 'A')
B_label = Label(root, text = 'B')
C_label = Label(root, text = 'C')
U_label = Label(root, text = 'U')

A_label.place(x = 200, y = 208)
B_label.place(x = 200, y = 268)
C_label.place(x = 200, y = 328)
U_label.place(x = 200, y = 388)

setpower_label = Label(root, text = "POWER")
setpower_label.place(x = 180, y = 118)

next_stage_label = Label(root, text = r'')
next_stage_label.place(x = 130, y = 88)


#RadionButtons
rand = StringVar()
rand.set(0)
go = rand.get()
Radiobutton(root, text = 'Random', command = lambda: select(),
                        variable = rand, value = "Random").place(x = 130, y = 50)
Radiobutton(root, text = 'By Hand', command = lambda: select(),
                         variable = rand, value = "Norm").place(x = 210, y = 50)


# Info Button
info_button = Button(root, text='press me for info', command=lambda: My_variat())
info_button.place(x=300, y=125)

# More buttons for collision
Search_image = PhotoImage(file=r"C:\Users\Oleh\codes\images\Bbb.png")

win2_button = Button(root, text='Open window 2', cursor='hand2', state = DISABLED)
win3_button = Button(root, text='Open window 3', cursor='hand2', state = DISABLED)
win4_button = Button(root, text='Open window 4', cursor='hand2', state = DISABLED)
win5_button = Button(root, text='Open window 5', cursor='hand2', state = DISABLED)


start = Button(root, text = "Задати множину", padx = 5,state= DISABLED,  command = lambda: action2())
start.place(x = 20, y = 180)

win2_button.place(x=300, y=10)
win3_button.place(x=300, y=35)
win4_button.place(x=300, y=60)
win5_button.place(x=300, y=85)



# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------


# Variant
def My_variat():
    G = 11
    N = 1
    variant = (N + G % 60) % 30 + 1
    speech = "Бєлов Олег\nМоя група: IO - 11\nМій номер у групі: 1\n" \
             "Мій варіант:" + str(variant)
    outputlabels.outlabel(0, speech, False, 0, 0)



# a class that out put any text on window "New Application by Oleh Bielov"
class outputlabels():
    def __init__(self, string, inp, div, x, y,):
        self.inp = inp
        self.x = x
        self.y = y
        self.div = div
        self.string = string

    # def on_click(x):
    #    if x == 'label':
    #        x.after(1000, label.destroy())

    def outlabel(self, inp, string, x, y):
        if string:
            text = Label(root, text=string + str(inp))
            text.place(x = x, y = y)
        else:    
            text = Label(root, text=inp)
            text.place(x = x, y = y)



def select():
    go = rand.get() 
    if go == "Random":
        next_stage_label.configure(text = r'Введіть потужність для множин')
        proccesing_button = Button(root, text = 'Дія', bg = 'yellow', command = lambda: action(main_set, setpower.get()))
        proccesing_button.place(x = 190, y = 165)
        start.configure(state=NORMAL)
    elif go == "Norm":
        start.configure(state=NORMAL)
        

def random_mode(A, B, C):
    global setA, setB, setC, setU
    setA = set(sample(range(20), A))
    setB = set(sample(range(20), B))
    setC = set(sample(range(20), C))
    setU = set(union(union(setA, setB), setC))
    outputlabels.outlabel(0, setA, 'A:  ', 0, 230) #x = 140, y = 230
    outputlabels.outlabel(0, setB, 'B:  ', 0, 290) #x = 140, y = 290
    outputlabels.outlabel(0, setC, 'C:  ', 0, 350) #x = 140, y = 350
    outputlabels.outlabel(0, setU, 'U:  ', 0, 410) #x = 140, y = 410

def normal_mode():
    global setA, setB, setC, setU
    setU = union(union(setA, setB), setC)
    win2_button.configure(state= NORMAL)
    outputlabels.outlabel(0, setA, 'A:  ', 0, 230) #x = 140, y = 230
    outputlabels.outlabel(0, setB, 'B:  ', 0, 290) #x = 140, y = 290
    outputlabels.outlabel(0, setC, 'C:  ', 0, 350) #x = 140, y = 350
    outputlabels.outlabel(0, setU, 'U:  ', 0, 410) #x = 140, y = 410


def action2():
    global setA, setB, setC, setU, powerA, powerB, powerC, mass
    go = rand.get() 
    if go == "Norm":
        try:
            setA = set(rbA.get().split(sep= ' ', maxsplit=10))
            setB = set(rbB.get().split(sep= ' ', maxsplit=10))
            setC = set(rbC.get().split(sep= ' ', maxsplit=10))
            maxValue = max(int(max(setA)), int(max(setB)), int(max(setC)))
            minValue = min(int(min(setA)), int(min(setB)), int(min(setC)))
            if maxValue <= 255 and minValue >=0:
                normal_mode()
            else:
                messagebox.showerror("Помилка", "Неправельно введені дані")
        except:
            messagebox.showerror("Помилка", "Неправельно введені дані")
    elif go == "Random":
        try:
            for i in range(len(main_set)):
                if i == 0:
                    powerA = int(main_set[i])
                elif i == 1:
                    powerB = int(main_set[i])
                elif i == 2:
                    powerC = int(main_set[i])    
        except:
            messagebox.showerror("Помилка", "Неправельно введені дані")
        random_mode(powerA, powerB,powerC)


def action(base_set, x):
    try:
        int_value = int(x)
        setpower.delete(0, END)
        base_set.append(int_value)

    except ValueError:
        messagebox.showerror("wrong")


root.mainloop()