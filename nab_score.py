import requests

def get_scoreboard_for_today():
    # Example working endpoint hosted on cdn.nba.com
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://www.nba.com',
        'Referer': 'https://www.nba.com'
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get('scoreboard', {}).get('games', [])

if __name__ == "__main__":
    games = get_scoreboard_for_today()
    for game in games:
        print(game.get('gameId'), game.get('homeTeam', {}).get('teamName'),
              "vs", game.get('awayTeam', {}).get('teamName'))
