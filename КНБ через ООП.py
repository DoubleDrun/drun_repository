from tkinter import *
from random import randint

"""
Я добавил изменение
"""


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.startUI(root)

    def startUI(self, root):
        btn = Button(root, text="Камень", font=("Times New Roman", 15), command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15), command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Бумага", font=("Times New Roman", 15), command=lambda x=3: self.btn_click(x))

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.lbl = Label(root, text="Начало игры!", bg="white", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.draw = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13), bg="white", text=f"Побед: {self.win}\n"
                                                                                            f"Проигрышей: {self.lose}\n"
                                                                                            f"Ничьих: {self.draw}")
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choice):
        # 1 - камень, 2  - ножницы, 3 - бумага
        comp_choice = randint(1, 3)
        print(comp_choice)

        if choice == comp_choice:
            self.draw += 1
            self.lbl.config(text="Ничья!")
        elif comp_choice == 1 and choice == 3 or comp_choice == 2 and choice == 1 or comp_choice == 3 and choice == 2:
            self.win += 1
            self.lbl.config(text="Победа!")
        else:
            self.lose += 1
            self.lbl.config(text="Проигрыш!")

        self.lbl2.config(text=f"Побед: {self.win}\n"
                              f"Проигрышей: {self.lose}\n"
                              f"Ничьих: {self.draw}")

        del comp_choice



window = Tk()
window.geometry("430x160+200+200")
window.title("Камень, ножницы, бумага")
window.resizable(False, False)
window["bg"] = "white"
# либо window.config(bg="white")

window2 = Tk()
window2.geometry("430x160+200+200")
window2.title("Камень, ножницы, бумага")
window2.resizable(False, False)
window2["bg"] = "white"


app = Main(window)
app.pack()

app2 = Main(window2)
app2.pack()


window.mainloop()
