habits = []
print("***Simple Habit Tracker*** ")

# Collect habit names
while True:
    name = input("Enter habit name (or press Enter to finish): ")
    if name == "":
        break
    habits.append({'name': name, 'done': False})

print("Habits added!")
if len(habits) == 0:
    print("No habits added today ")
else:
    print("Today's Habits:")
    for i, h in enumerate(habits):
        print(f"{i+1}. {h['name']} [Pending]")

# Mark habits as done or not
for i, h in enumerate(habits):
    mark = input(f"Did you complete '{h['name']}' today? (y/n): ").lower()
    if mark == 'y':
        h['done'] = True
        print("Good nice job ")
    elif mark == 'n':
        print(" work hard ")

# Show summary
num = sum(1 for h in habits if h['done'])
total = len(habits)
if total > 0:
    print(f"Habits completed: {num}/{total} ({num/total*100:.1f}%)")
else:
    print("***No habits to track today***")
print("***Keep up the good work***")