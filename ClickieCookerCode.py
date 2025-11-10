import tkinter as tk
class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Clickie Cooker")
        self.window.geometry("400x600+550+100")
        self.image = tk.PhotoImage(file="background.png")
        self.cursor = "@cursor.cur"
        self.window.config(cursor=self.cursor)
        self.imageLabel = tk.Label(self.window, image=self.image)
        self.imageLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.scoreValue = 0
        self.scoreText = tk.Label(self.window, text=f"Your score: {self.scoreValue}", font=("Arial", 20, "bold"), bg="white")
        self.scoreText.place(x=100, y=40)
        self.scoreText.lift()
        self.window.resizable(False, False)
        self.imageLabel.place_configure(relwidth="", relheight="")
        self.window.update_idletasks()
        self.origin_x = (400 - self.image.width()) // 2
        self.origin_y = (600 - self.image.height()) // 2
        self.imageLabel.place(x=self.origin_x, y=self.origin_y)
        self.imageLabel.bind("<Button-1>", self.AddScore)
        self.window.mainloop()

    def AddScore(self, event):
        self.scoreValue += 1
        self.scoreText.config(text=f"Your score: {self.scoreValue}")
        self.AnimationLoop()
        self.ColorChange()

    def AnimationLoop(self):
        offsets = [10, -10, 6, -6, 3, -3, 0]
        self.Shake(offsets, 0)

    def Shake(self, offsets, index):
        if index >= len(offsets):
            return
        dx = offsets[index]
        self.imageLabel.place(x=self.origin_x + dx, y=self.origin_y)
        self.window.after(30, lambda: self.Shake(offsets, index + 1))

    def ColorChange(self):
            if 0<self.scoreValue<=100:
                self.scoreText.config(fg="green")
            elif 100<self.scoreValue<=200:
                self.scoreText.config(fg="blue")
            elif 200<self.scoreValue<=500:
                self.scoreText.config(fg="gray")
            else: self.scoreText.config(fg="red")
Main()
