import sys

# Function to analyze cat shelter logs
def analyze_cat_shelter(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Initialize counters
            total_our_cat_visits, total_intruder_visits, total_time_spent = 0, 0, 0
            visit_lengths = []

            for line in file:
                # Stop reading if the 'END' marker is found
                if line.strip() == 'END':
                    break

                # Split each line into cat type, entry and exit times
                cat_type, entry_time, exit_time = line.split(',')
                entry_time, exit_time = int(entry_time), int(exit_time)
                visit_duration = exit_time - entry_time

                # Count and record stats for our cat
                if cat_type == 'OURS':
                    total_our_cat_visits += 1
                    total_time_spent += visit_duration
                    visit_lengths.append(visit_duration)
                else:
                    # Count intruder cat visits
                    total_intruder_visits += 1

            # Calculate statistics
            if total_our_cat_visits > 0:
                average_duration = total_time_spent // total_our_cat_visits
                longest_visit = max(visit_lengths)
                shortest_visit = min(visit_lengths)
            else:
                average_duration = longest_visit = shortest_visit = 0

            # Convert total time spent to hours and minutes
            hours, minutes = divmod(total_time_spent, 60)

            # Return the calculated statistics
            return {
                'total_our_cat_visits': total_our_cat_visits,
                'total_intruder_visits': total_intruder_visits,
                'hours': hours,
                'minutes': minutes,
                'average_duration': average_duration,
                'longest_visit': longest_visit,
                'shortest_visit': shortest_visit
            }, None

    except FileNotFoundError:
        # Handle the case where the file is not found
        return None, f'Cannot open "{filename}"!'
    
# Check for the correct number of command line arguments
if len(sys.argv) != 2:
    print("Missing command line argument!")
    sys.exit(1)

# Get the filename from command line arguments
filename = sys.argv[1]
data, error = analyze_cat_shelter(filename)

# Print the results or the error message
if error:
    print(error)
else:
    print("\nLog File Analysis")
    print("===================")
    print("===================\n")
    print(f"Cat Visits: {data['total_our_cat_visits']}")
    print(f"cats have been doused with water.: {data['total_intruder_visits']}\n")
    print(f"Total Time in House: {data['hours']} Hours, {data['minutes']} Minutes\n")
    print(f"Average Visit Length: {data['average_duration']} Minutes")
    print(f"Longest Visit length: {data['longest_visit']} Minutes")
    print(f"Shortest Visit length: {data['shortest_visit']} Minutes")

