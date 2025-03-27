"""
Library for connecting to sports APIs for live updates
=======================================================================================

This library utilizes Adafruit libraries to send requests to the NBA API, process the returned JSON data,
format time information, and determine whether a game is current or scheduled for the future. Based on these
decisions, it invokes appropriate functions from the draw_tools library.

Author(s): Michael Ladderbush
"""

import wifi
import socketpool
import ssl
import adafruit_requests
from draw_tools import draw_future_game

# Initialize HTTP request support with SSL.
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, ssl_context)

# NBA scoreboard API endpoint URL.
NBA_SCOREBOARD_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

def fetch_celtics_game():
    try:
        response = requests.get(NBA_SCOREBOARD_URL)
        data = response.json()
        response.close()

        # Retrieve the list of games from the JSON response.
        games = data.get("scoreboard", {}).get("games", [])
        for game in games:
            home_team = game["homeTeam"]["teamName"]
            away_team = game["awayTeam"]["teamName"]

            # Check if either team is the Celtics.
            if home_team == "Celtics" or away_team == "Celtics":
                home_score = game["homeTeam"]["score"]
                away_score = game["awayTeam"]["score"]
                clock = game["gameClock"]
                return home_score, away_score, clock

        # Return default values if no Celtics game is found.
        return -1, -1, "00:00"

    except Exception as e:
        print("Failed to fetch NBA games:", e)
        return 0, 0, "12:00"

def get_current_date():
    TIMEZONE = "America/New_York"
    URL = f"http://worldtimeapi.org/api/timezone/{TIMEZONE}"

    response = requests.get(URL)
    time_data = response.json()
    response.close()

    # Extract the date portion ("YYYY-MM-DD") from the ISO datetime string.
    datetime_str = time_data["datetime"]
    date_part = datetime_str.split("T")[0]
    year, month, day = date_part.split("-")
    
    month = int(month)
    day = int(day)
    # Convert the date into the NBA schedule format.
    current_date = (month * 31) - 3
    current_date = current_date + day
    
    return current_date

def get_current_time():
    TIMEZONE = "America/New_York"
    URL = f"http://worldtimeapi.org/api/timezone/{TIMEZONE}"
    
    response = requests.get(URL)
    time_data = response.json()
    response.close()
    
    # Extract the ISO datetime string from the API response.
    datetime_str = time_data["datetime"]
    
    # Convert the ISO datetime string to a datetime object.
    dt = datetime.fromisoformat(datetime_str)
    
    # Format the time as "HH:MM AM/PM" and remove any leading zero from the hour.
    formatted_time = dt.strftime("%I:%M %p").lstrip("0")
    
    return formatted_time

def get_next_game():
    # Determine today's game based on the NBA schedule format.
    game_today = False
    current_date = get_current_date()

    while game_today == False:
        nba_schedule = {
            100: {"time": "8:30 PM", "location": "home (vs)", "opponent": "Los Angeles"},
            100: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Utah"},
            102: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Oklahoma City"},
            104: {"time": "7:00 PM", "location": "away (@)", "opponent": "Miami"},
            105: {"time": "6:00 PM", "location": "away (@)", "opponent": "Brooklyn"},
            108: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Brooklyn"},
            111: {"time": "9:30 PM", "location": "away (@)", "opponent": "Utah"},
            113: {"time": "6:00 PM", "location": "away (@)", "opponent": "Portland"},
            114: {"time": "10:00 PM", "location": "away (@)", "opponent": "Sacramento"},
            116: {"time": "10:00 PM", "location": "away (@)", "opponent": "Phoenix"},
            120: {"time": "8:00 PM", "location": "away (@)", "opponent": "San Antonio"},
            122: {"time": "7:30 PM", "location": "away (@)", "opponent": "Memphis"},
            124: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Miami"},
            126: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Phoenix"},
            128: {"time": "6:00 PM", "location": "home (vs)", "opponent": "Washington"},
            130: {"time": "7:30 PM", "location": "away (@)", "opponent": "New York"},
            131: {"time": "7:00 PM", "location": "away (@)", "opponent": "Orlando"},
            133: {"time": "7:30 PM", "location": "home (vs)", "opponent": "Charlotte"},
            135: {"time": "1:00 PM", "location": "home (vs)", "opponent": "Charlotte"}
        }

        try:
            game_info = nba_schedule.get(current_date)
            if game_info is None:
                # Increment the current date if no game is found for this date.
                current_date = current_date + 1
            else:
                print("Found next game")
                print(game_info)
                game_date = current_date
                game_time = game_info.get("time", "unknown time")
                game_location = game_info.get("location", "unknown location")
                game_opponent = game_info.get("opponent", "unknown opponent")
                draw_future_game(game_date, game_time, game_location, game_opponent)
                game_today = True
        except:
            break
