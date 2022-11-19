from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._player1 = Player(player1_name)
        self._player2 = Player(player2_name)
        self._score_map = {
            'ties': ['Love-All', 'Fifteen-All', 'Thirty-All', 'Forty-All', 'Deuce'],
            'names': ['Love', 'Fifteen', 'Thirty', 'Forty']
        }
        self._players_by_name = {
            player1_name: self._player1,
            player2_name: self._player2,
        }

    def won_point(self, player_name: str):
        self._players_by_name[player_name].add_point()

    def get_score(self):
        leader_score, score_difference, leading_player = self._get_score_status()
        if self._is_tied(score_difference):
            score = self._score_map['ties'][min(leader_score, 4)]
        elif self._is_advantage(score_difference, leader_score):
            score = f"Advantage {leading_player.name}"
        elif self._is_win(score_difference, leader_score):
            score = f"Win for {leading_player.name}"
        else:
            score = f"{self._score_map['names'][self._player1.points]}-{self._score_map['names'][self._player2.points]}"

        return score

    def _is_tied(self, score_diff):
        return score_diff == 0
    
    def _is_advantage(self, score_diff, max_score):
        return max_score >= 4 and score_diff == 1

    def _is_win(self, score_diff, max_score):
        return max_score >= 4 and score_diff >= 2
    
    def _get_score_status(self):
        max_points = max(self._player2.points, self._player1.points)
        min_points = min(self._player2.points, self._player1.points)
        leader = None if max_points == 0 else max(self._player1, self._player2, key=lambda p: p.points)
        return (max_points, max_points - min_points, leader)
