def read_runner_data(filename):
    """Read runner data from a file."""
    runners = []
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) != 3:
                    raise ValueError("Invalid data format")
                name = data[0]
                lap1_time = float(data[1])
                lap2_time = float(data[2])
                runners.append((name, lap1_time, lap2_time))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    return runners

def write_runner_data(runners, filename):
    """Write runner data to a file."""
    with open(filename, "w") as file:
        file.write("Runner Name, Progresses to Next Stage\n")
        for runner in runners:
            file.write(f"{runner[0]}, {runner[1]}\n")

def progress_to_next_stage(runners):
    """Determine which runners progress to the next stage."""
    progressing_runners = []
    for runner in runners:
        if runner[1] < 50 or runner[2] < 50:  # Checking if any of the laps is less than 50 seconds
            progressing_runners.append((runner[0], "Yes"))
        else:
            progressing_runners.append((runner[0], "No"))
    return progressing_runners

def find_fastest_runner(runners):
    """Find the runner with the fastest lap."""
    fastest_lap = min(min(runner[1], runner[2]) for runner in runners)
    for runner in runners:
        if min(runner[1], runner[2]) == fastest_lap:
            return runner[0], fastest_lap

def count_occurrences(runners):
    """Count occurrences of each lap time."""
    occurrences = {}
    for runner in runners:
        lap1_time = runner[1]
        lap2_time = runner[2]
        occurrences[lap1_time] = occurrences.get(lap1_time, 0) + 1
        occurrences[lap2_time] = occurrences.get(lap2_time, 0) + 1
    return occurrences

def sort_runners_by_lap_time(runners):
    """Sort runners by their lap times."""
    return sorted(runners, key=lambda x: min(x[1], x[2]))

def main():
    print("Scottish Athletics 400m Trials - Female Group")
    print("-----------------------------------------------------")

    # Read runner data from file - for input validation
    runners = read_runner_data("runners.txt")

    if runners:
        # Find runners who progress to the next stage
        progressing_runners = progress_to_next_stage(runners)

        # Find the fastest runner
        fastest_runner, fastest_lap_time = find_fastest_runner(runners)

        # Output results
        print(f"Fastest lap was completed by {fastest_runner} in {fastest_lap_time} seconds")
        print("Runner Name           Progresses to Next Stage")
        for runner in progressing_runners:
            print(f"{runner[0]:<22} {runner[1]}")

        # Write runner results to a file
        write_runner_data(progressing_runners, "runners_results.txt")

        # Count occurrences of each lap time
        lap_occurrences = count_occurrences(runners)
        print("\nOccurrences of each lap time:")
        for lap_time, occurrence in lap_occurrences.items():
            print(f"Lap time {lap_time}: {occurrence} occurrence(s)")

        # Sort runners by their lap times
        sorted_runners = sort_runners_by_lap_time(runners)
        print("\nRunners sorted by their lap times:")
        for runner in sorted_runners:
            print(f"{runner[0]}: {min(runner[1], runner[2])} seconds")

if __name__ == "__main__":
    main()
