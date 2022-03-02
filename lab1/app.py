from tkinter import *
from tkinter import messagebox
from functions import *
from random import sample


main_set = []


class MODES:
    def __init__(self, x):
        pass



# a class that out put any text on window "New Application by Oleh Bielov"
class outputlabels():
    def __init__(self, inp):
        self.inp = inp

    # def on_click(x):
    #    if x == 'label':
    #        x.after(1000, label.destroy())

    def outlabel(self, inp):
        text = Label(root, text=inp)
        text.grid(row=5, column=0)


def select():
    go = rand.get()
    if go == "Random":
        setpower.configure(state = NORMAL)
        next_stage_label.configure(text = r'Введіть потужність для множин')
        proccesing_button = Button(root, text = 'Дія', bg = 'yellow', command = lambda: action(setpower.get()))
        proccesing_button.place(x = 190, y = 165)   
    elif go == "Norm":
        rbA.configure(state = NORMAL)
        rbB.configure(state = NORMAL) 
        rbC.configure(state = NORMAL)
        rbU.configure(state = NORMAL)
#123123
def action(x):
    try:
        count = 0
        int_value = int(x)
        while count < 4:
            setpower.configure(state = NORMAL)
            setpower.delete(0, END)
            main_set.append(int_value)
            count = count + 1
        if count == '3':
            setpower.configure(state = DISABLED)
    except ValueError:
        messagebox.showerror("wrong")


# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------
root = Tk()
root.title("New Application by Oleh Bielov")
root.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
root.geometry("400x500")

# Variant
def My_variat():
    G = 11
    N = 1
    variant = (N + G % 60) % 30 + 1
    speech = "Бєлов Олег\nМоя група: IO - 11\nМій номер у групі: 1\n" \
             "Мій варіант:" + str(variant)
    outputlabels.outlabel(0, speech)


# Exit Button
exit_button = Button(root, text="exit", command=root.quit)
exit_button.place(x=360, y=370)

#Entry viget
rbA = Entry(root, borderwidth = 5, state = DISABLED)
rbA.place(x = 140, y = 230)
rbB = Entry(root, borderwidth = 5, state = DISABLED)
rbB.place(x = 140, y = 290)
rbC = Entry(root, borderwidth = 5, state = DISABLED)
rbC.place(x = 140, y = 350)
rbU = Entry(root, borderwidth = 5, state = DISABLED)
rbU.place(x = 140, y = 410)


setpower = Entry(root, borderwidth = 5, state = DISABLED)
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


win2_button.place(x=300, y=10)
win3_button.place(x=300, y=35)
win4_button.place(x=300, y=60)
win5_button.place(x=300, y=85)



# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------
root.mainloop()