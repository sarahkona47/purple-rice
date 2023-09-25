# ------------------ Import statements -------------------
import tkinter as tk

# --------------------------------------------------------
class Window:
    self.mainWin = tk.Tk()

    self.otherWin = tk.Toplevel(self.mainWin)
        self.otherWin.title("Chicken Gambling Simulator")
        welcomeLabel = tk.Label(self.otherWin,
                                text="Welcome to our Chicken Gambling Simulator \n",
                                font="Arial 24",
                                bg="white",
                                fg="black",
                                justify=tk.CENTER)
        welcomeLabel.grid(row=0, column=0, columnspan = 11)
        creatorsLabel = tk.Label(self.otherWin,
                                    text="Created by: Sarah Choi, Daniel Seo, Eunice Lim \n",
                                    font="Arial 18",
                                    bg="white",
                                    fg="black",
                                    justify=tk.CENTER)
    def run(self):
        """This function runs the program."""
        self.mainWin.mainloop()

#----------------- Main Program --------------------------
win = Window()
win.run()