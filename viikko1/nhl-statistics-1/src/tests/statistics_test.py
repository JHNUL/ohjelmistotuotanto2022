import unittest

from statistics import Statistics
from player import Player

test_players = [
    Player("Semenko", "EDM", 4, 12),
    Player("Lemieux", "PIT", 45, 54),
    Player("Kurri",   "EDM", 37, 53),
    Player("Yzerman", "DET", 42, 56),
    Player("Gretzky", "EDM", 35, 89)
]


class PlayerReaderStub:
    def get_players(self):
        return test_players


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(reader=PlayerReaderStub())

    def test_players_fetched_in_constructor(self):
        instance_players = list(map(str, self.statistics._players))
        expected_players = list(map(str, test_players))
        self.assertListEqual(instance_players, expected_players)

    def test_search_finds_player(self):
        player = self.statistics.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_does_not_find_player(self):
        player = self.statistics.search("Jon Snow")
        self.assertIsNone(player)

    def test_lists_all_players_in_team(self):
        team = self.statistics.team("EDM")
        self.assertIsInstance(team, list)
        self.assertEqual(len(team), 3)
        names = list(map(lambda playah: playah.name, team))
        self.assertListEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_lists_all_players_in_team_nonexistent_team(self):
        team = self.statistics.team("karhukissat")
        self.assertIsInstance(team, list)
        self.assertEqual(len(team), 0)

    def test_top_with_negative_number(self):
        top = self.statistics.top(-12)
        self.assertIsInstance(top, list)
        self.assertEqual(len(top), 0)

    def test_top_player_is_found(self):
        top = self.statistics.top(0)
        self.assertIsInstance(top, list)
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0].name, "Gretzky")
