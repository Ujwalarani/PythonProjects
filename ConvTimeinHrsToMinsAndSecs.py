"""Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds."""

time_hours = float(input("Enter time (in hours): "))

# Conversion of given time from Hours to Minutes and Seconds

time_mins = time_hours * 60
mins = int(time_mins)
time_secs = round((time_mins - mins) * 60)
print(f"{time_hours} hours is equal to {mins} minutes and {time_secs} seconds")
