from tkinter import *
from random import *
import copy


root = Tk()
root.title("lab2")
root.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
root.geometry("300x300")


#a program that is intended for declaring my variant
def set_my_variant():
    G = 11
    i = 1
    M = "IB"
    if M == "IO":
        i += 2
    variant = ((i + G % 60) % 30 + 1)
    return "Бєлов Олег\nМоя група: IO - 11\nМій номер у групі: 1\n" \
           "Мій варіант:" + str(variant)



#-------------------------Parent------------------------------

class Setup:    
    def __init__(self, win2 = 'root2', win3 = 'root3', win4 = 'root4'):
        self.win2 = win2
        self.win3 = win3
        self.win4 = win4
        self.set_W = ['Ірина', 'Анна', 'Зоя', 'Олена', 'Марія', 'Юлія', 'Дарина', 'Інна', 'Катерина',]
        self.set_M = ['Богдан', 'Ілля', 'Данило', 'Даніїл', 'Олександр', 'Віталій', 'Андрій', 'Артем', 'Владислав']
        return self.win2, self.win3, self.win4, self.set_W, self.set_M

#-------------------------Parent------------------------------



#-------------------------WINDOW2-------------------------------

class Window2(Setup):
    def __init__(self):
        super(Window2, self).__init__()

    def space2(self):
        global female, text_A, text_B, female_save, val, male, male_save, win2_btn_save 
        self.win2 = Toplevel()
        self.win2.title("Window2")
        self.win2.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
        self.win2.geometry("450x500")

        female = ''
        male = ''
        female_save = {}
        male_save = {}


        win2_listbox1 = Listbox(self.win2, height = 10, selectmode = MULTIPLE)
        win2_listbox2 = Listbox(self.win2, height = 10, selectmode = MULTIPLE)

        val = StringVar()
        Radiobutton(self.win2, text = 'A', variable = val, value = 'female').place(x = 160, y = 150)
        Radiobutton(self.win2, text = 'B', variable = val, value = 'male').place(x = 200, y = 150)

        text_A = Label(self.win2, text = 'A = {}')
        text_B = Label(self.win2, text = 'B = {}')
        text_A.place(x = 0, y = 200)
        text_B.place(x = 0, y = 220)

        for i in self.set_W:
            win2_listbox1.insert(END, i)


        for i in self.set_M:
            win2_listbox2.insert(END, i)

        win2_listbox2.place(x = 300, y = 0)
        win2_listbox1.place(x = 0, y = 0)


        win2_btn = Button(self.win2, text = 'ADD', command = lambda: add()).pack()
        win2_btn_delete = Button(self.win2, text = "delete from set", command = lambda: delete()).pack()

        win2_btn_save = Button(self.win2, text = "Зберегти", state = NORMAL, command = lambda: save()).pack()

        win2_btn_clear_A = Button(self.win2, text = 'Очистити А', command = lambda: clear_A()).pack()
        win2_btn_clear_B = Button(self.win2, text = 'Очистити B', command = lambda: clear_B()).pack() 

        def add():
            global female, male, text_A, text_B, female_save, val, male_save
            #all females names saved in female instance above
            if val.get() == 'female':
                try:
                    female_save = female.copy() 
                    female = ''
                except AttributeError:
                    pass
                
                for item in win2_listbox1.curselection():
                    if win2_listbox1.get(item) in self.set_W:
                        female = female + str(win2_listbox1.get(item)) + ' '
                    else:
                        break
                
                for item in win2_listbox2.curselection():
                    if win2_listbox2.get(item) in self.set_M:
                        female = female + str(win2_listbox2.get(item)) + ' '
                    else:
                        break
                female = set(female.split())
                female = female.union(female_save)
                text_A.configure(text = 'A = '  + str(female))
            elif val.get() == 'male':
                #all males names saved in male instance above
                try:
                    male_save = male.copy() 
                    male = ''
                except AttributeError:
                    pass
                    
                for item in win2_listbox1.curselection():
                    if win2_listbox1.get(item) in self.set_W:
                        male = male + str(win2_listbox1.get(item)) + ' '
                    else:
                        break
                
                for item in win2_listbox2.curselection():
                    if win2_listbox2.get(item) in self.set_M:
                        male = male + str(win2_listbox2.get(item)) + ' '
                    else:
                        break

                male = set(male.split())
                male = male.union(male_save)
                text_B.configure(text = 'B = '  + str(male))

        def delete():
            global female, text_A, val, male, text_B
            if val.get() == 'female':
                for i in win2_listbox1.curselection():
                    if win2_listbox1.get(i) in female:
                        female.discard(win2_listbox1.get(i))
                    else:
                        break
                
                for i in win2_listbox2.curselection():
                    if win2_listbox2.get(i) in female:
                        female.discard(win2_listbox2.get(i))
                text_A.configure(text = 'A = ' + str(female))
            elif val.get() == 'male':
                for i in win2_listbox1.curselection():
                    if win2_listbox1.get(i) in male:
                        male.discard(win2_listbox1.get(i))
                    else:
                        break
                
                for i in win2_listbox2.curselection():
                    if win2_listbox2.get(i) in male:
                        male.discard(win2_listbox2.get(i))
                text_B.configure(text = 'B = ' + str(male))


        def clear_A():
            global text_A, female, female_save
            female = ''
            female_save = {}
            text_A.configure(text = 'A = {}'.format(female))


        def clear_B():
            global text_B, male, male_save
            male = ''
            male_save = {}
            text_B.configure(text = 'B = '.format(male))

        def save():
            global female, male, win2_btn_save
            with open(r'C:\Users\Oleh\git\lab2\saved.txt', 'w') as f:
                f.write(str(female), )
                f.write('\n')
                f.write(str(male))
                f.write('\n')


        self.win2.mainloop()
#-------------------------WINDOW2-------------------------------

#-------------------------WINDOW3-------------------------------

class Window3(Setup):


    def __init__(self):
        super(Window3, self).__init__()
            

    def space3(self):
        global win3_listbox1, win3_listbox2
        self.win3 = Toplevel()
        self.win3.title("Window2")
        self.win3.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
        self.win3.geometry("620x628")

        win3_btn = Button(self.win3, text = 'розрахувати алгорит S', command = lambda: algorithmS()).place(x = 10, y = 10)
        win3_btn = Button(self.win3, text = 'розрахувати алгорит R', command = lambda: algorithmR()).place(x = 10, y = 40)
        win3_btn = Button(self.win3, text = 'відобразити на малюнку', command = lambda: canvas_aSb()).place(x = 10, y = 70)
        
        win3_lbl_frame1 =LabelFrame(self.win3, text = 'aSb')
        win3_lbl_frame2 = LabelFrame(self.win3, text = 'aRb')
        win3_lbl_frame1.place(x = 200, y = 0)
        win3_lbl_frame2.place(x = 400, y = 0)
        win3_listbox1 = Listbox(win3_lbl_frame1, height = 10, selectmode=DISABLED)
        win3_listbox1.pack()
        win3_listbox2 = Listbox(win3_lbl_frame2, height = 10, selectmode=DISABLED)
        win3_listbox2.pack()

        def algorithmS():
            global relationsS, win3_listbox1
            god_father = list()
            for i in female:
                if i in self.set_M:
                    god_father.append(i)
            
            copy_god_father = god_father.copy()
            relationsS = set()
            B = male.copy()
            while len(relationsS) < len(copy_god_father):
                father = choice(list(god_father))
                child = choice(list(B))
                god_father.remove(father)
                if father == child:
                    B.remove(child)
                    child = choice(list(B))
                if (child, father) not in relationsS:
                    relationsS.add((father, child))
                    B.remove(child)
                if len(god_father) == 0:
                    break 
            print(relationsS)
            for i in relationsS:
                win3_listbox1.insert(END, str(i) + ',')
            return relationsS

        def algorithmR():
            global relationsS, relationsR, win3_listbox2
            svoyak = list()
            for i in female:
                if i in self.set_M:
                    svoyak.append(i)
             
            copy_svoyak = svoyak.copy()
            relationsR = set()
            B = male.copy()
            while len(relationsR) < len(copy_svoyak):
                bridegroom = choice(list(svoyak))
                boyfriend = choice(list(B))
                svoyak.remove(bridegroom)
                if bridegroom == boyfriend:
                    B.remove(boyfriend)
                    boyfriend = choice(list(B))
                if boyfriend in self.set_W:
                    B.remove(boyfriend)
                    boyfriend = choice(list(B))    
                if bridegroom and boyfriend in self.set_M:
                    if (bridegroom, boyfriend) not in relationsS:
                        relationsR.add((bridegroom, boyfriend))
                        B.remove(boyfriend)
                if len(svoyak) == 0:
                    break
            print(relationsR)  
            for i in relationsR:
                win3_listbox2.insert(END, str(i) + ',')
            return relationsR

        def canvas_aSb():
            global relationsR, relationsS
            aSb = Canvas(self.win3, width=700, height=200)
            dict_SA = {}
            dict_SB = {}
            for i in range(len(female)):
                aSb.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_SA.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                aSb.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                aSb.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_SB.update({list(male)[x]: [30 + x * 50, 160]})
            for k in relationsS:
                aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow = LAST)
            aSb.place(x = 50, y = 150)
            aRb = Canvas(self.win3, width=700, height=225)
            dict_RA = {}
            dict_RB = {}
            for i in range(len(female)):
                aRb.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_RA.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                aRb.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                aRb.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_RB.update({list(male)[x]: [30 + x * 50, 160]})
            for k in relationsR:
                aRb.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow = LAST)
            aRb.place(x = 50, y = 400)
            lbl_aSb = Label(self.win3, text = 'a хрещений батько b: ', font=('New Times Roman', 10))
            lbl_aSb.place(x = 50, y = 147)
            lbl_aRb = Label(self.win3, text = 'а свояк b:', font=('New Times Roman', 10))
            lbl_aRb.place(x = 50, y = 397) 
        

        self.win3.mainloop()

#-------------------------WINDOW3-------------------------------



#-------------------------WINDOW4-------------------------------

class Window4(Setup):


    def __init__(self):
        super(Window4, self).__init__()


    def space4(self):
        self.win4 = Toplevel()
        self.win4.title("Window2")
        self.win4.iconbitmap(r"C:\Users\Oleh\codes\index.ico")
        self.win4.geometry("550x500")
        win4_frame = Frame(self.win4, bd = 10)
        win4_frame.place(x= 90, y = 0)
        win4_lbl_oper = Label(win4_frame, text = 'Операції над відношеннями', font = ('Arial', 16))
        win4_lbl_oper.grid(row = 0, columnspan=4)
        #¬  ∩  ∪
        union_btn = Button(self.win4, text = 'R ∪ S', width=5, command = lambda: btn1())
        union_btn.grid(row = 1, column=0, sticky='w')
        intersiction_btn = Button(self.win4, text = 'R ∩ S', width = 5, command = lambda: btn2())
        intersiction_btn.grid(row = 2, column=0, sticky='w')
        difference_btn = Button(self.win4, text ='R \ S', width=5, command=lambda: btn3())
        difference_btn.grid(row = 3, column=0, sticky='w')
        not_btn  =Button(self.win4, text = 'U \ R', width=5, command = lambda: btn4())
        not_btn.grid(row =4, column=0, sticky='w')
        reverse_btn = Button(self.win4, text = 'S-1', width=5, command = lambda: btn5())
        reverse_btn.grid(row = 5, column=0, sticky='w')
        canv = Canvas(self.win4, width=600, height=250)
        canv.grid(row = 1, rowspan=6, column=3)


        def btn1():
            canv.delete('all')
            canv.create_text(150, 20, text = 'R \u222A S', font = 'Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = list(relationsR) + list(relationsS)
            for i in range(len(female)):
                canv.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_b1.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                canv.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                canv.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_b2.update({list(male)[x]: [30 + x * 50, 160]})
            for l in V:
                canv.create_line(dict_b1[l[0]], dict_b2[l[1]], arrow = LAST)

        def btn2():
            canv.delete('all')
            canv.create_text(150, 20, text = 'R \u2229 S', font = 'Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = []
            for i in relationsR:
                if i in relationsS:
                    V.append(i)
            for i in range(len(female)):
                canv.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_b1.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                canv.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                canv.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_b2.update({list(male)[x]: [30 + x * 50, 160]})
            for l in V:
                if len(V) != 0:
                    canv.create_line(dict_b1[l[0]], dict_b2[l[1]], arrow = LAST)
            

        def btn3():
            canv.delete('all')
            canv.create_text(150, 20, text = 'R \u2229 S', font = 'Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(relationsR)
            for i in V:
                if i in relationsS:
                    V.remove(i)
            for i in range(len(female)):
                canv.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_b1.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                canv.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                canv.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_b2.update({list(male)[x]: [30 + x * 50, 160]})
            for l in V:
                canv.create_line(dict_b1[l[0]], dict_b2[l[1]], arrow = LAST)
            

        def btn4():
            canv.delete('all')
            canv.create_text(150, 20, text = 'R \u2229 S', font = 'Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = relationsS
            for i in range(len(female)):
                canv.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_b1.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                canv.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                canv.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_b2.update({list(male)[x]: [30 + x * 50, 160]})
            for l in V:
                if len(V) != 0:
                    canv.create_line(dict_b1[l[0]], dict_b2[l[1]], arrow = LAST)
            
        def btn5():
            canv.delete('all')
            canv.create_text(150, 20, text = 'R \u2229 S', font = 'Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(relationsS)
            print(V)
            for i in V:
                list(i)[0], list(i)[1] = list(i)[1], list(i)[0]
            print(V)
            for i in range(len(female)):
                canv.create_text(30 + i * 50, 50, text=list(female)[i], font=("New Times Roman", 10))
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill='yellow')
                dict_b1.update({list(female)[i]: [30 + i * 50, 80]})
            for x in range(len(male)):
                canv.create_text(30 + x * 50, 190, text=list(male)[x], font=("New Times Roman", 10))
                canv.create_oval([20 + x * 50, 160], [40 + x * 50, 140], fill='red')
                dict_b2.update({list(male)[x]: [30 + x * 50, 160]})
            for l in V:
                canv.create_line(dict_b1[l[0]], dict_b2[l[1]], arrow = LAST)
            
        self.win4.mainloop()
#-------------------------WINDOW4-------------------------------



#-------------------------WINDOW1------------------------------

txt = Label(root, text = set_my_variant(), font = ('new times roman', 16))
txt.place(x = 55, y = 0) 

look2 = Window2()
look3 = Window3()
look4 = Window4()

btn2 = Button(root, text = 'Window 2', activebackground='yellow', padx = 20, command = lambda: look2.space2()).place(x= 95, y = 105)
btn3 = Button(root, text = 'Window 3', activebackground='yellow', padx = 20, command = lambda: look3.space3()).place(x= 95, y = 130)
btn4 = Button(root, text = 'Window 4', activebackground='yellow', padx = 20, command = lambda: look4.space4()).place(x= 95, y = 155)

#-------------------------WINDOW1------------------------------

root.mainloop()
