# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Pomodoro Timer application that helps improve productivity with time management. It implements countdown timers for work and break intervals with sound notifications when complete.

## Running the Application

```bash
# Run the main application
python main.py
```

## Project Structure

- **main.py** - Contains the complete Pomodoro timer implementation
- **.idea/** - PyCharm/IntelliJ IDE configuration files

## Key Technical Details

### Cross-Platform Sound Support
The application uses platform-specific sound implementations:
- **Windows**: `winsound.Beep()` for beep notifications
- **Mac**: `afplay` command with system sound files (`/System/Library/Sounds/Glass.aiff`)
- **Linux**: Terminal bell character (`\a`)

### Features
- Configurable number of Pomodoro sessions
- Customizable work and break durations
- Countdown timer with MM:SS display
- 5-second warning notification before work session ends
- Cross-platform sound notifications at end of work/break periods

### Core Dependencies
- `time` - For countdown timer functionality and sleep
- `sys` - For platform detection
- `winsound` - Windows-specific sound (conditional import)
- `os` - For system commands (macOS sound playback)

## Development Notes

- This is a single-file Python application with no external package dependencies
- The application runs in the terminal/command line
- Sound functionality is platform-specific and may need adaptation for non-Windows systems
- The `.idea/` directory contains IDE settings and should not be modified manually
