import time
import tkinter as tk
import random

# Dictionary for rigged probabilities 
probability = {}

def rigged_timer():
    global probability 
    # Total probability
    total_probability = sum(probability.values())

    print(f"Start")

    # Start crash
    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Stop time based on probabilities
        if random.random() < total_probability:
            stop_time = random.choices(list(probability.keys()), list(probability.values()))[0]
            if elapsed_time >= stop_time:
                break

        # Start from 1x incremental increase
        display_time = (elapsed_time * 0.1) + 1
        print(f"{display_time:.2f}x", end="\r")

        # Make timer visualization smooth
        sleep_time = min(0.01, 0.5 - (current_time - start_time) % 0.5)
        time.sleep(sleep_time)

    print("\nCrash")

if __name__ == "__main__":
    # Probabilities based on grouping of min - max times
    probability_ranges = [
        {"min_time": 2, "max_time": 5, "total_probability": 0.02}, # 30% crash  # currently only taking in first probability range
        {"min_time": 8, "max_time": 14, "total_probability": 0.4}, # 40% crash
        {"min_time": 14, "max_time": 17, "total_probability": 0.3}, # 30% crash
        {"min_time": 18, "max_time": 25, "total_probability": 0.2}, # 20% crash
        {"min_time": 30, "max_time": 70, "total_probability": 0.05}, # 5% crash
        {"min_time": 75, "max_time": 100, "total_probability": 0.01} # 1% crash
    ]

    for range_info in probability_ranges:
        min_time = range_info["min_time"]
        max_time = range_info["max_time"]
        total_probability = range_info["total_probability"]

        num_intervals = max_time - min_time + 1

    for time_interval in range(min_time, max_time + 1):
        probability[time_interval] = total_probability / num_intervals

    rigged_timer()
