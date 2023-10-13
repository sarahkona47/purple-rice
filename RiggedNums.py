import time
import random

# List to store intervals
intervals = []
previous_crashes = []

def simulate_crash():
    global intervals, previous_crashes

    # Start crash
    start_time = time.time()
    print("Start")

    while intervals:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= intervals[0]:
            crashed_interval = intervals.pop(0)
            previous_crashes.append(elapsed_time)

        # Start from 1x incremental increase
        display_time = (elapsed_time * 0.1) + 1
        print(f"{display_time:.2f}x", end="\r")
        

        # Make timer visualization smooth
        sleep_time = min(0.01, 0.5 - (current_time - start_time) % 0.5)
        time.sleep(sleep_time)

    print("\nCrash")
    print("Previous crashes:")
    for crash_time in previous_crashes:
        print(f"Crashed at {crash_time:.2f}x")

if __name__ == "__main__":
    # Probabilities based on grouping of min - max times
    probability_ranges = [
        {"min_time": 2, "max_time": 5, "total_probability": 0.1},  # 2-5: 10% crash
        {"min_time": 8, "max_time": 14, "total_probability": 0.1},  # 8-14: 10% crash
        {"min_time": 16, "max_time": 25, "total_probability": 0.1},  # 16-25: 10% crash
        {"min_time": 30, "max_time": 35, "total_probability": 0.1},  # 30-35: 10% crash
        {"min_time": 40, "max_time": 45, "total_probability": 0.1},  # 40-45: 10% crash
        {"min_time": 50, "max_time": 55, "total_probability": 0.1},  # 50-55: 10% crash
    ]

    while True:
        for range_info in probability_ranges:
            min_time = range_info["min_time"]
            max_time = range_info["max_time"]
            total_probability = range_info["total_probability"]

            num_intervals = max_time - min_time + 1

            # Calculate the number of intervals based on the total probability
            num_intervals_in_range = int(total_probability * num_intervals)

            for _ in range(num_intervals_in_range):
                intervals.append(random.randint(min_time, max_time))

        random.shuffle(intervals)  # Shuffle the intervals to randomize their order

        simulate_crash()
        time.sleep(10)   # 10 second delay before crash starts again
