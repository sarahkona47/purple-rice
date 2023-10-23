import time
import random

# List to store intervals
intervals = []
previous_crashes = []


# All numbers are just pseudo. Subject to any changes. This is test document.

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
            previous_crashes.append(crashed_interval)

            # Break out of the loop after the first crash
            break

        # Make timer visualization smooth
        sleep_time = min(0.01, 0.5 - (current_time - start_time) % 0.5)
        time.sleep(sleep_time)

    print("\nCrash")
    print("Previous crashes:")
    for crash_time in previous_crashes:
        print(f"Crashed at {crash_time:.2f}x")

def generate_intervals(probability_ranges):
    intervals = []
    for range_info in probability_ranges:
        min_time = range_info["min_time"]
        max_time = range_info["max_time"]
        total_probability = range_info["total_probability"]

        # Calculate the number of intervals based on the total probability
        num_intervals_in_range = int(total_probability * 100)  # Assuming probabilities as percentages

        for _ in range(num_intervals_in_range):
            intervals.append(round(random.uniform(min_time, max_time), 2))

    random.shuffle(intervals)  # Shuffle the intervals to randomize their order
    return intervals

if __name__ == "__main__":
    # Probabilities based on grouping of min - max times (as percentages)
    probability_ranges = [
        {"min_time": 1.00, "max_time": 1.50, "total_probability": 0.05},  # 2.00-3.00: 10% crash
        {"min_time": 1.50, "max_time": 2.10, "total_probability": 0.50},  # 2.00-3.00: 10% crash
        {"min_time": 3.00, "max_time": 4.00, "total_probability": 0.1},  # 3.00-4.00: 10% crash
        {"min_time": 4.00, "max_time": 5.00, "total_probability": 0.1},  # 4.00-5.00: 10% crash
        {"min_time": 5.00, "max_time": 6.00, "total_probability": 0.07},  # 5.00-6.00: 10% crash
    ]

    while True:
        intervals = generate_intervals(probability_ranges)
        simulate_crash()
        time.sleep(1)  # 1-second delay before crash starts again
