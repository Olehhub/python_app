from tkinter import *
from tkinter import messagebox
from functions import *
from random import sample



def mode():
    global arrA, arrB, arrC, univU, u, powerA, powerB, powerC, i, j
    try:
        with open(r"C:\Users\Oleh\codes\RESULT.txt") as f:
            f.read()
    except FileNotFoundError or FileExistsError:
        print("Нажаль, заданого програмою файлу не існує")

    i = 1
    j = 1
    value = rand.get()
    if value == "Hand":
        try:
            arrA = set(re.split(r"[,::\s]", arrA.get()))
            arrB = set(re.split(r"[,::\s]", arrB.get()))
            arrC = set(re.split(r"[,::\s]", arrC.get()))
            maxV = max(int(max(arrA)), int(max(arrB)), int(max(arrC)))
            minV = min(int(min(arrA)), int(min(arrB)), int(min(arrC)))
            if maxV <= 255 and minV >= 0:
                MODES.normode()
                win2_button.configure(state = NORMAL)
                win3_button.configure(state = NORMAL)
                win4_button.configure(state = NORMAL)
                win5_button.configure(state = NORMAL)
            else:
                messagebox.showerror('Помилка', 'Неправильно введені дані')



        except:
            messagebox.showerror("Помилка", 'Неправильно введені дані')

    elif value == "Random":
        try:
            powerA = int(arrA.get())
            powerB = int(arrB.get())
            powerC = int(arrC.get())
        except ValueError:
            messagebox.showerror(
                "Помилка", 'Неправильно введені дані'
            )
        maxV = max(powerA, powerB, powerC)
        a = univU.get()
        u = a.split(' ')
        if len(u) == 2:
            u1 = int(u[0])
            u2 = int(u[1])
            if u1 > u2 or ((u2 - u1) < maxV or u2 > 255):
                messagebox.showerror("Помилка", 'Неправильно введені дані')
            else:
                MODES.randomMode()
                win2_button.configure(state=NORMAL)
                win3_button.configure(state=NORMAL)
                win4_button.configure(state=NORMAL)
                win5_button.configure(state=NORMAL)

# need some time to do this code, pay close attention to this function
# if i choose a "Random" radionbutton, then i want to some entry space pop up
# and i could put there info for algorithm
def select():
    value = rand.get()
    if value == "Random":
        button.configure(text='Згенерувати множину')
        button.configure(state = NORMAL)
        e_vig1.configure(state = NORMAL)
        e_vig2.configure(state = NORMAL)
        e_vig3.configure(state = NORMAL)
        e_vig4.configure(state = NORMAL)
        label.configure(text = "Введіть потужніть множин \nІнтервал для U-множини")
    elif value == "Hand":
        button.configure(text='Задати множину')
        button.configure(state = NORMAL)
        e_vig1.configure(state = NORMAL)
        e_vig2.configure(state = NORMAL)
        e_vig3.configure(state = NORMAL)
        e_vig4.configure(state = DISABLED)
        label.configure(text = "Введіть елементи доя множин")



class MODES:


    def normode(self):
        global univU
        univU = union(union(arrA, arrB), arrC)
        win2_button.configure(state = NORMAL)
        printer()


    def randomMode(self):
        global arrA, arrB, arrC, arrU

        arrU = list()

        for i in range(int(u[0]), int(u[1]), - int(u[0]) + 2):
            arrU.append(i)
        arrA = sample(arrU, powerA)
        arrB = sample(arrU, powerB)
        arrC = sample(arrU, powerC)
        univU = union(union(arrA, arrB), arrC)
        printer()




def printer():
    results.configure(text = "A: " + str(arrA) +
                      "\n\nB: " + str(arrB) +
                      "\n\nC: " + str(arrC) +
                      "\n\nU: " + str(univU))

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


# ----------------------------------------------------
# ---------------------MainWindow---------------------
# ----------------------------------------------------
root = Tk()
root.title("New Application by Oleh Bielov")
root.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
root.geometry("400x400")


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
results = Label(root, text = '')
results.place(x = 50, y = 50)

label = Label(root, text = '')
label.place(x = 140, y = 100)

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
button = Button(root, text = "Дія", state = DISABLED, command = lambda: mode())


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