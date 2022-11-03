from datetime import datetime

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    reader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    stats = PlayerStats(reader)
    nationality = "FIN"
    players = stats.top_scorers_by_nationality(nationality)

    print(f"Players from {nationality} {datetime.isoformat(datetime.now())}:\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
