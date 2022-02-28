from tkinter import *
from tkinter import messagebox
from functions import *
from random import sample



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
    pass

# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------
root = Tk()
root.title("New Application by Oleh Bielov")
root.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
root.geometry("400x400")

#12312
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
e_vig1 = Entry(root, borderwidth = 5, state = DISABLED)
e_vig1.place(x = 140, y = 170)
e_vig2 = Entry(root, borderwidth = 5, state = DISABLED)
e_vig2.place(x = 140, y = 230)
e_vig3 = Entry(root, borderwidth = 5, state = DISABLED)
e_vig3.place(x = 140, y = 290)
e_vig4 = Entry(root, borderwidth = 5, state = DISABLED)
e_vig4.place(x = 140, y = 350)


#Some Labels
txt_label = Label(root, text = "Виберіть мод")
txt_label.place(x = 165, y = 20)

A_label = Label(root, text = 'A')
B_label = Label(root, text = 'B')
C_label = Label(root, text = 'C')
U_label = Label(root, text = 'U')

A_label.place(x = 200, y = 148)
B_label.place(x = 200, y = 208)
C_label.place(x = 200, y = 268)
U_label.place(x = 200, y = 328)

#RadionButtons
rand = StringVar()
rand.set(0)
Radiobutton(root, text = 'Random', command = lambda: select(),
                        variable = rand, value = "Random").place(x = 130, y = 50)
Radiobutton(root, text = 'By Hand', command = lambda: select(),
                         variable = rand, value = "Hand").place(x = 210, y = 50)


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