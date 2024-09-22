# daily_reminder.py

# Prompt user for a single task
task = input("Enter your task: ")

# Prompt user for task priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = "Invalid priority level."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += " Consider completing it when you have free time."

# Print the reminder
print(reminder_message)
