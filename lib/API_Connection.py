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
            game_id = game["gameId"]
            home_team = game["homeTeam"]["teamName"]
            away_team = game["awayTeam"]["teamName"]

            # Check if either team is the Celtics.
            if home_team == "Celtics":
                home_score, away_score, clock = get_scoreboard(game_id)
                return home_score, away_score, away_team, clock

            if away_team == "Celtics":
                home_score, away_score, clock = get_scoreboard(game_id)
                return home_score, away_score, home_team, clock

        # Return default values if no Celtics game is found.
        return -1, -1, "unknown", "00:00"

    except Exception as e:
        print("Failed to fetch NBA games:", e)
        return 0, 0, "unknown", "12:00"

def get_current_date():
    TIMEZONE = "America/New_York"
    URL = f"http://worldtimeapi.org/api/timezone/{TIMEZONE}"

    response = requests.get(URL)
    print(response)
    time_data = response.json()
    print(time_data)
    response.close()

    #TODO: Update the json parsing

    iso = time_data["datetime"].split("T")[0]
    y,m,d = iso.split("-")
    return int(y), int(m), int(d)

def add_one_day(year, month, day):

    days_in_month = [31, 29 if (year%4==0 and (year%100!=0 or year%400==0)) else 28,
           31,30,31,30,31,31,30,31,30,31]
    day += 1

    if day > days_in_month[month-1]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

    return year, month, day


#TODO: on off-day update to include new API
def get_next_game():
    team_name = "Celtics"
    year, month, day = get_current_date()
    if year is None:
        print("Couldnt get date")
        return

    for _ in range(60):
        ymd = f"{year:04d}{month:02d}{day:02d}"
        url = f"https://data.nba.net/data/10s/prod/v1/{ymd}/scoreboard.json"

        try:
            response = requests.get(url, timeout = 5)
            json = response.json() if getattr(response, "status_code", None) == 200 else{}
        except Exception as e:
            print(f"Network error on {ymd}:", e)
            json = {}
        finally:
            response.close()

        games = json.get("scoreboard", {}).get("games", json.get("games", []))

        for game in games:
            if(game["homeTeam"]["teamName"] == team_name or
               game["awayTeam"]["teamName"] == team_name):
                if g["homeTeam"]["teamName"] == team_name:
                    loc = "home (vs)"
                    opp = f"{game['awayTeam']['teamCity']} {game['awayTeam']['teamName']}"
                else:
                    loc = "away (@)"
                    opp = f"{game['homeTeam']['teamCity']} {game['homeTeam']['teamName']}"
                
                tip = game.get("gameStatusText") or game.get("gameEt") or "TBD"
                date_str = f"{year}-{month:02d}-{day:02d}"

                draw_future_game(date_str, tip, loc, opp)
                return
            
        year, month, day = add_one_day(year, month, day)
        print("No game found in next 60 days")

def accept_IOS_input(str: http_request):
    return http_request


def get_scoreboard(game_id):

    NBA_SCOREBOARD_URL = f"https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

    response = requests.get(NBA_SCOREBOARD_URL)
    data = response.json()
    response.close()

    games = data.get("scoreboard", {}).get("games", [])
    for game in games:
        game_id = game["gameId"]
        game_clock = game["gameClock"]
        home_team_struct = game["homeTeam"]
        home_team_name = home_team_struct["teamName"]
        away_team_struct = game["awayTeam"]
        away_team_name = away_team_struct["teamName"]

        if home_team_name == "Celtics":
            home_score = home_team_struct["score"]
            away_score = away_team_struct["score"]

        if away_team_name == "Celtics":
            away_score = home_team_struct["score"]
            home_score = away_team_struct["score"]

        if home_score is not None and away_score is not None and game_clock:
            return int(home_score), int(away_score), game_clock

    return 0, 0, "0:00"


