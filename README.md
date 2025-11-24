# Simple tasks Tracker

A command-line Python script designed to help you track your daily habits, mark them as done or pending, and see your completion progress for the day. Simple, interactive, and ideal for personal use or as a beginner Python project!

## Features

- Add any number of new habits for today.
- Mark each habit as complete or pending.
- View a summary of your daily progress at the end.
- Encouraging feedback for your efforts!

## How to Use

1. **Clone the repository:**
    ```bash
    git clone https://github.com/diddukunta25bmr10007-collab/simple-tasks-tracker-.git
    cd simple-tasks-tracker-
    ```

2. **Run the script:**
    ```bash
    python habit_tracker.py
    ```
   *(Make sure you are using Python 3.)*

3. **Follow the prompts:**
   - Enter names for your habits. Leave the input empty and press Enter when done.
   - For each habit, answer whether you completed it today by typing `y` or `n`.
   - At the end, see how many habits you completed and your completion percentage.

## Example

```
***Simple Habit Tracker***

Enter habit name (or press Enter to finish): Drink Water
Enter habit name (or press Enter to finish): Meditate
Enter habit name (or press Enter to finish):

Habits added!
Today's Habits:
1. Drink Water [Pending]
2. Meditate [Pending]
Did you complete 'Drink Water' today? (y/n): y
Good, nice job!
Did you complete 'Meditate' today? (y/n): n
Work hard!

Habits completed: 1/2 (50.0%)
***Keep up the good work!***
```

## Customization and Improvements

- **Input validation**: Ensures proper responses.
- **Persistent storage**: You can upgrade the script to save/load habits to a file or database.
- **More statistics**: Track progress over multiple days/weeks.

Feel free to contribute or suggest enhancements!

## License

This project is open source and available under the [MIT License](LICENSE).
