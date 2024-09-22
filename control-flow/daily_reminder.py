task = input("Enter the task: ")
priority = input("Enter task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task is time-bound ? (yes or no): ").lower()

message = ""
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = f"Invalid priority level."

if time_bound == 'yes':
    message += f" It requires immediate attention today!"
elif time_bound == 'no':
    message +=  f" Consider completing it when you have free time."
else:
    message += f" Invalid time_bound"

print(message)
