class PlayerStats:
    def __init__(self, reader) -> None:
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        players_list = list(filter(lambda p: p.nationality == nationality, players))
        players_list.sort(key=lambda p: p.get_points(), reverse=True)
        return players_list
