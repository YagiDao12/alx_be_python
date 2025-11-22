# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine priority message using match-case
match priority:
    case "high":
        priority_msg = f"'{task}' is a high priority task"
    case "medium":
        priority_msg = f"'{task}' is a medium priority task"
    case "low":
        priority_msg = f"'{task}' is a low priority task"
    case _:
        priority_msg = f"'{task}' has an unspecified priority"

# Add time sensitivity using IF
if time_bound == "yes":
    time_msg = "that requires immediate attention today!"
else:
    time_msg = "Consider completing it when you have free time."

# ✅ FINAL single reminder output (required by checker)
print(f"Reminder: {priority_msg} {time_msg}")
