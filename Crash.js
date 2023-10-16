// Declare Variables
const intervals = [];
const previous_crashes = [];
const probability_ranges = [
    {"min_time": 2, "max_time": 5, "total_probability": 0.1},  // 2-5: 10% crash
    {"min_time": 8, "max_time": 14, "total_probability": 0.1},  // 8-14: 10% crash
    {"min_time": 16, "max_time": 25, "total_probability": 0.1},  // 16-25: 10% crash
    {"min_time": 30, "max_time": 35, "total_probability": 0.1},  // 30-35: 10% crash
    {"min_time": 40, "max_time": 45, "total_probability": 0.1},  // 40-45: 10% crash
    {"min_time": 50, "max_time": 55, "total_probability": 0.1},  // 50-55: 10% crash
    ];


//Sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

// Timer function
async function timer() {
    const start_time = Date.now;
    console.log("start");

    while (intervals >= 0){
        const current_time = Date.now;
        elapsed_time = new Date();
        elapsed_time = current_time - start_time;
        if(elapsed_time >= intervals[0]){
            const crashed_interval = new Array();
            crashed_interval = intervals.pop(0);
        }
        
        displaytime = (elapsedTime * 0.1) + 1
        console.log(displaytime.toFixed(2));

        sleep_time = new Date();
        sleep_time = min(0.01, 0.5 - (current_time - start_time) % 0.5)
        await sleep(sleep_time);

        console.log("\nCrash")
        console.log("Previous crashes:")
        for (crash_time in previous_crashes){
            print("Crashed at", displaytime.toFixed(2), "x")
        }
        
    }

}

// Multiplier

timer()

