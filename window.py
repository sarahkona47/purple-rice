# ------------------ Import statements -------------------
import tkinter as tk
from functools import partial
# --------------------------------------------------------
class Window:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Chicken Gambling Simulator")
        self.myCanvas = tk.Canvas(self.win, bg="purple", height=250, width=300)
        self.myCanvas.pack()
        self.win.mainloop()

#----------------- Main Program --------------------------
window = Window()
window.run()