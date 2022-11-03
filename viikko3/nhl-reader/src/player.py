class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self._name = name
        self._team = team
        self._goals = int(goals)
        self._assists = int(assists)
        self._nationality = nationality
    
    def get_points(self):
        return self._goals + self._assists

    @property
    def name(self):
        return self._name

    @property
    def team(self):
        return self._team

    @property
    def goals(self):
        return self._goals

    @property
    def assists(self):
        return self._assists

    @property
    def nationality(self):
        return self._nationality

    def __str__(self):
        return f"{self.name:<25}{self.nationality:<5}{self.goals:2} + {self.assists:2} ={self.get_points():3}"
