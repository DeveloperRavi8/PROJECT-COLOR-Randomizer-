from tkinter import *
import random

root = Tk()
root.title("Color Randomizer")
root.geometry("500x500")
root.configure(background="Blue")


class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.list = ['yellow', 'black', 'white', 'red', 'orange', 'gray', 'purple', 'cyan']
        self.color = [
            "#FFFF00",
            "#000000",
            "#FFFFFF",
            "#FF0000",
            "#FFA500",
            "#808080",
            "#800080",
            "#00FFFF" 
        ]
        self.random_number_for_text = random.randint(0, 7)
        self.random_number_for_color = random.randint(0, 7)
        label['text'] = self.list[self.random_number_for_text]
        label['fg'] = self.color[self.random_number_for_color]


label = Label(root, text="COLOR", background="blue", fg="white", font=("Viner Hand ITC", 30, "bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)

gameObj = game()


button = Button(root, text="Start", command=gameObj.updateGame, bg="darkblue", relief=FLAT, padx=10, pady=10)
button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()