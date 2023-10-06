# ------------------ Import statements -------------------
import tkinter as tk
# --------------------------------------------------------
class Window:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Chicken Gambling Simulator")
        self.myCanvas = tk.Canvas(self.win, bg="white", height=700, width=1080)
    
        entry = tk.Entry(self.win)
        entry.place(x=540, y=500)

        bet_text = tk.Label(self.win, bg = "white", text = "Place your bet", font=("Helvetica", 24))
        bet_text.place(x=350, y=500)

        timer_label = tk.Label(self.win, bg = "white", text="Multiplier 0.0", font=("Helvetica", 30))
        timer_label.place(x=500, y=300)

        bet_button = tk.Button(text = "Enter")
        bet_button.place(x=700, y=500)


        self.myCanvas.pack()

        self.win.mainloop()
        

        
#----------------- Main Program --------------------------
window = Window()
window.run()