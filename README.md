# NBA Scoreboard Display

## Overview
The NBA Scoreboard Display is a CircuitPython-based project designed to control an Adafruit Matrix display and present live NBA game updates in a visually engaging manner. The project connects to WiFi, queries the official NBA API for live game data (with a current focus on the Celtics), and renders dynamic scoreboard graphics including scores, game time, and scheduled future games.

## Features
- **Live Game Updates:** Automatically retrieves real-time NBA game data.
- **Dynamic Display:** Updates scores, game clocks, and game dates on an LED matrix.
- **Future Game Scheduling:** Displays details of upcoming games based on a predefined schedule when no live game is detected.
- **Custom Graphics Rendering:** Utilizes CircuitPython's `displayio` to render team logos, numbers, and other graphics.
- **Modular Design:** Separates API connections, drawing functions, and application logic for ease of customization and maintenance.

## Customization
- **Team Selection:** While the current configuration focuses on the Celtics, you can modify the code in the API and drawing modules to support other teams.
- **Display Settings:** Tweak timing intervals, graphic dimensions, and other visual elements in the source code to suit your specific requirements.

## Acknowledgments
- **Adafruit:** For providing excellent hardware, libraries, and tutorials.
- **Community Support:** Thanks to the members of the Adafruit Forums, Stack Overflow, and Reddit for their invaluable support and inspiration.
- **NBA:** For offering public access to game data.

