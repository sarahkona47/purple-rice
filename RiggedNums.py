import time;
import tkinter as tk;
import random;

# Need to add initial multiplier for crash
# Need multiplier increase rate
# Need average time to crash/probability for crash/cash-out probabilities (like 70% for most then rest)


# Probability for timer to stop
# probability = [(1, 1.5, 0.05), (1.5, 2, 0.3), (2, 4, 0.1)] # add more probability later
def rigged_timer(probability):
    # Calculate the total probability for all time intervals
    total_probability = sum(probability.values())
    
    print(f"Start")
    
    # Start the timer
    start_time = time.time()
    
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Check if the timer should stop based on the specified probabilities
        if random.random() < total_probability:
            stop_time = random.choices(list(probability.keys()), list(probability.values()))[0]
            if elapsed_time >= stop_time:
                break
        
        # Display the elapsed time at a rate of 0.5 seconds per second
        display_time = elapsed_time * 0.5
        print(f"{display_time:.2f}x", end="\r")
        
        # Adjust the sleep time for smoother updates
        sleep_time = min(0.01, 0.5 - (current_time - start_time) % 0.5)
        time.sleep(sleep_time)
    
    print("\nCrash")

if __name__ == "__main__":
    # Probability in crash times
    probability = {
        5: 0.2,  # 20% 5 sec
        8: 0.3,  # 30% 8 sec
        10: 0.5  # 50% 10 sec
    }
    
    rigged_timer(probability)
