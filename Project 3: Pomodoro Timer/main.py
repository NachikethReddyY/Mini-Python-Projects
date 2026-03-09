"""
### 3. **Study Timer (Pomodoro Timer)**
- **Need:** Improve productivity with time management.
- **Modules Needed:** `time`, `winsound` (Windows) or `os` (Mac/Linux)
- **Description:** A simple countdown timer with work and break intervals. Plays a sound when done.
- **Challenges:** Time management, cross-platform sound support.
"""

import time
import sys
import os

"""
Steps to Solve this:
    Ask the user for input, how many Pomodoro sessions they want.
    Check if it is a number.

    Ask the user for input, how much time in minutes for work.
    Check if it is a number.
    Ask the user for input, how much time for break in minutes.
    Check if it is a number.

    For each session:
        Start the countdown for work time.
        Give a message at the last 5 seconds.

        Check the OS, Mac or Windows (use conditional imports for winsound).
        Play the sound when work session ends.

        Start the break countdown (no warnings, just relax).

        Once Break Ends play the sound.

    Exit after all sessions complete.
"""

# Ask the user for Input
print("Welcome to Pomodoro Timer built with python!")
# how many Pomodoro sessions they want
sessions = input("How many sessions would you like to work? ")
# Ask the user for input
minutes = input("How many minutes would you like to work in each session? ")
breaks = input("How many minutes would you like to break between sessions? ")

def countdown(seconds, label=""):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer_display = f"{mins:02d}:{secs:02d}"
        if label:
            print(f"[{label}] {timer_display}", end="\r")
        else:
            print(f"{timer_display}", end="\r")

        # Give a message at the last 5 seconds
        if seconds == 5:
            print(f"\n⏰ 5 seconds remaining!")

        time.sleep(1)
        seconds -= 1
    print("00:00 - Time's up!     ")

def play_sound():
    if sys.platform == "win32":
        import winsound
        winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms
    elif sys.platform == "darwin":
        # macOS - use afplay with a system sound
        os.system("afplay /System/Library/Sounds/Glass.aiff")
    else:
        # Linux - use echo with bell character
        print("\a")

if sessions.isdigit() and minutes.isdigit() and breaks.isdigit():
    sessions = int(sessions)
    work_seconds = int(minutes) * 60
    break_seconds = int(breaks) * 60
    for i in range(1, sessions + 1):
        print(f"\n🍅 Session {i} of {sessions} — Work!")
        countdown(work_seconds, label="work")
        play_sound()

        print(f"☕ Break time!")
        countdown(break_seconds)       # No warning label for breaks
        play_sound()
    print("\n✅ All sessions complete! Great work!")
else:
    print("❌ Please enter valid whole numbers.")


