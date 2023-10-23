const intervals = [];
const previousCrashes = [];

function simulateCrash() {
    // Start crash
    const startTime = Date.now();
    console.log("Start");

    const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    (async function loop() {
        while (intervals.length > 0) {
            const currentTime = Date.now();
            const elapsed_time = (currentTime - startTime) / 1000; // Convert to seconds

            if (elapsed_time >= intervals[0]) {
                const crashedInterval = intervals.shift();
                previousCrashes.push(crashedInterval);

                console.log("\nCrash");
                console.log(`Crashed at ${crashedInterval.toFixed(2)}x`);
                console.log("Previous crashes:");
                for (const crashTime of previousCrashes) {
                    console.log(`Crashed at ${crashTime.toFixed(2)}x`);
                }

                // Break out of the loop after the first crash
                break;
            }

            // Make timer visualization smooth
            const sleepTime = Math.min(10, 500 - (currentTime - startTime) % 500);
            await sleep(sleepTime);
        }
    })();
}

function generateIntervals(probabilityRanges) {
    const intervals = [];
    for (const rangeInfo of probabilityRanges) {
        const minTime = rangeInfo.minTime;
        const maxTime = rangeInfo.maxTime;
        const totalProbability = rangeInfo.totalProbability;

        // Calculate the number of intervals based on the total probability
        const numIntervalsInRange = Math.round(totalProbability * 100); // Assuming probabilities as percentages

        for (let i = 0; i < numIntervalsInRange; i++) {
            intervals.push(parseFloat((Math.random() * (maxTime - minTime) + minTime).toFixed(2)));
        }
    }

    shuffleArray(intervals); // Shuffle the intervals to randomize their order
    return intervals;
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Probabilities based on grouping of min - max times (as percentages)
const probabilityRanges = [
    { minTime: 1.00, maxTime: 1.50, totalProbability: 0.05 }, // 2.00-3.00: 5% crash
    { minTime: 1.50, maxTime: 2.00, totalProbability: 0.60 }, // 2.00-3.00: 60% crash
    { minTime: 3.00, maxTime: 4.00, totalProbability: 0.08 }, // 3.00-4.00: 8% crash
    { minTime: 4.00, maxTime: 5.00, totalProbability: 0.1 }, // 4.00-5.00: 10% crash
    { minTime: 5.00, maxTime: 6.00, totalProbability: 0.08 }, // 5.00-6.00: 8% crash
    { minTime: 6.00, maxTime: 20.00, totalProbability: 0.04 }, // 6.00-20.00: 4% crash
];

(function main() {
    // Continuously simulate crashes
    (async function loop() {
        while (true) {
            intervals.length = 0; // Clear intervals for each iteration
            intervals.push(...generateIntervals(probabilityRanges));
            await simulateCrash();
            await sleep(1000); // 1-second delay before the next crash simulation
        }
    })();
})();
