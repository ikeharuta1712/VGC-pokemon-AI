# Written by BUI VU KHOA

from VGUBattlePolicy import VGUPolicy
from vgc.behaviour import BattlePolicy
from vgc.competition.Competitor import Competitor
from vgc.behaviour import BattlePolicy, TeamSelectionPolicy, TeamBuildPolicy
from vgc.behaviour.BattlePolicies import RandomPlayer, TerminalPlayer
from vgc.behaviour.TeamBuildPolicies import TerminalTeamBuilder, RandomTeamBuilder
from vgc.behaviour.TeamSelectionPolicies import FirstEditionTeamSelectionPolicy
from vgc.competition.Competitor import Competitor

class VGUComp(Competitor):

    def __init__(self, name: str = "VGUbot"):
        self._name = name
        self._battle_policy = VGUPolicy()

    @property
    def name(self):
        return self._name

    @property
    def battle_policy(self) -> BattlePolicy:
        return self._battle_policy


# BELOW COMPETITORS ARE IMPORTED FOR TESTING PURPOSES
class ExampleCompetitor(Competitor):

    def __init__(self, name: str = "Example"):
        self._name = name
        self._battle_policy = RandomPlayer()

    @property
    def name(self):
        return self._name

    @property
    def battle_policy(self) -> BattlePolicy:
        return self._battle_policy