import tkinter as tk
class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Clickie Cooker")
        self.window.geometry("400x600+550+100")
        self.image = tk.PhotoImage(file="background.png")
        self.cursor = "@cursor.cur"
        self.imageLabel = tk.Label(self.window, image=self.image)
        self.imageLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.config(cursor=self.cursor)
        self.scoreValue = 0
        self.scoreText = tk.Label(self.window, text=f"Your score: {self.scoreValue}", font=("Arial", 20, "bold"), bg="white")
        self.scoreText.place(x=100, y=40)
        self.scoreText.lift()
        self.window.resizable(False, False)
        self.imageLabel.bind("<Button-1>", self.Addscore)
        self.window.mainloop()

    def Addscore(self, event):
        self.scoreValue +=1
        self.scoreText.config(text=f"Your score: {self.scoreValue}")
Main()