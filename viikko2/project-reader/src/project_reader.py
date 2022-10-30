from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        dc = toml.loads(content)
        return Project(
            dc["tool"]["poetry"]["name"],
            dc["tool"]["poetry"]["description"],
            dc["tool"]["poetry"]["dependencies"],
            dc["tool"]["poetry"]["dev-dependencies"]
        )
