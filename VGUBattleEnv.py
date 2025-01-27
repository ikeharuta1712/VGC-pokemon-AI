# Writter by BUI VU KHOA, DAO THE HIEN and NGUYEN DUNG in collaboration

from VGUCompetitor import VGUComp, ExampleCompetitor
from vgc.behaviour.BattlePolicies import GUIPlayer, TunedTreeTraversal, RandomPlayer, BreadthFirstSearch
from VGUBattlePolicy import VGUPolicy
from vgc.competition.BattleMatch import BattleMatch
from vgc.competition.Competitor import CompetitorManager
from vgc.util.generator.PkmRosterGenerators import RandomPkmRosterGenerator
from vgc.util.generator.PkmTeamGenerators import RandomTeamFromRoster
from vgc.engine.PkmBattleEnv import PkmBattleEnv
from multiprocessing.connection import Client

# runs a BO3 with the same team for both rounds

# BELOW IS CODE FOR THE TERMINAL MODE
# TO USE THE UI MODE, SEE BELOW

def main():
    roster = RandomPkmRosterGenerator().gen_roster()
    tg = RandomTeamFromRoster(roster)

    c0 = ExampleCompetitor("Player 1")
    c0._battle_policy = RandomPlayer() #Switch to GUI player for player control
    cm0 = CompetitorManager(c0)
    cm0.team = tg.get_team()

    c1 = VGUComp("Player VGU")
    c1._battle_policy = VGUPolicy()
    cm1 = CompetitorManager(c1)
    cm1.team = tg.get_team()

    match = BattleMatch(cm0, cm1, debug=True)
    match.run()  #run match by default settings


if __name__ == '__main__':
    main()


# BELOW IS CODE FOR THE UI MODE
# TO FULLY USE THE UI, YOU MUST FIRST RUN PkmBattleUX.py INSIDE THE pokemon-vgc-engine\vgc\ux FOLDER
# IF YOU ENABLE UI MODE, PLEASE DISABLE (COMMENT) THE CODE BLOCK ABOVE, AND VICE VERSA

# a0 = GUIPlayer()
# a1 = VGUPolicy()
# address = ('localhost', 6000) #localhose is needed as the game structure if using UI connects through the local server
# roster = RandomPkmRosterGenerator().gen_roster()
# tg = RandomTeamFromRoster(roster)
# full_team0 = tg.get_team()
# full_team1 = tg.get_team()
# conn = Client(address, authkey='VGC AI'.encode('utf-8'))
# env = PkmBattleEnv((full_team0.get_battle_team([0, 1, 2]), full_team1.get_battle_team([0, 1, 2])), debug=True,
#                    conn=conn, encode=(a0.requires_encode(), a1.requires_encode()))
# env.reset()
# t = False
# ep = 0
# n_battles = 1
# while ep < n_battles:
#     s, _ = env.reset()
#     env.render(mode='ux')
#     ep += 1
#     while not t:
#         a = [a0.get_action(s[0]), a1.get_action(s[1])]
#         s, _, t, _, _ = env.step(a)
#         env.render(mode='ux')
#     t = False
# env.close()