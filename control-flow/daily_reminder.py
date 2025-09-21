# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = print("Reminder: '{task}' is a high priority task")
    case "medium":
        reminder = print("Reminder: '{task}' is a medium priority task. Try to schedule it today.")
    case "low":
        reminder = print("Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        reminder = print("Reminder:'{task}' has an unknown priority level. Please review your input.")

# Modify the reminder if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder = print("Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")

# Print the customized reminder
print(reminder)
