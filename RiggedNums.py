import time;
import tkinter as tk;
import random;

# Need to add initial multiplier for crash
# Need multiplier increase rate
# Need average time to crash/probability for crash/cash-out probabilities (like 70% for most then rest)


# Probability for timer to stop
probability = [(1, 1.5, 0.05), (1.5, 2, 0.3), (2, 4, 0.1), ()] # add more probability later

# percentage of crashing between certain numners
def percentNum():

# Auto mode
def auto():

    
# Creates a timer
def random_timer():
    global intervals
    selected_interval = random.choices(intervals, [p for _, _, p in intervals])[0]
    start_time, end_time, _ = selected_interval
    random_duration = random.uniform(start_time, end_time)
    return random_duration

# This function stops the timer. 
def random_timer_stop():
    global timer_running, start_time
    if timer_running:
        timer_running = False
        stopped_time = time.time() - start_time
        timer_label.config(text=f"Stopped at {stopped_time:.2f} seconds")

# Starts the timer.
def timer_start():
    global timer_running, stop_timer
    if not timer_running:
        timer_running = True
        start_time = time.time()
        timer_label.config(text="Timer is running...")
        timer_duration = random_timer()
        root.after(int(timer_duration * 1000), stop_timer)

root = tk.Tk()
root.title("Random Timer")

timer_running = False
start_time = 0

timer_label = tk.Label(root, text="Click 'Start' to begin the timer.")
timer_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_timer)
stop_button.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

root.mainloop()