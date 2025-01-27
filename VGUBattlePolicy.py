# Writter by BUI VU KHOA, DAO THE HIEN, NGUYEN DUNG and PHAM TUAN KIET in collaboration

# THIS CODE WAS PARTIALLY REFERENCED FROM PUNISHER BOT, ONE OF THE LAST YEAR'S SUBMISSIONS AS WELL AS SEVERAL EXAMPLES PROVIDED BY THE COORDINATORS.
# However, we still had to make several additions and adjustments for it to work with our vision for the program.

from typing import List
import random

from vgc.behaviour import BattlePolicy
from vgc.datatypes.Objects import GameState, PkmMove
from vgc.datatypes.Types import PkmStat, PkmType, WeatherCondition, PkmStatus
from vgc.datatypes.Constants import DEFAULT_N_ACTIONS, DEFAULT_PKM_N_MOVES, TYPE_CHART_MULTIPLIER, DEFAULT_PARTY_SIZE

def damage_estimate(move_type: PkmType, pkm_type: PkmType, move_power: float, opp_pkm_type: PkmType, #the entire calculation for best damage and rreturning
                    attack_stage: int, defense_stage: int, move_pp: int) -> float:
    stab = 1.5 if move_type == pkm_type else 1.
    stage_level = attack_stage - defense_stage
    stage = (stage_level + 2.) / 2 if stage_level >= 0. else 2. / (np.abs(stage_level) + 2.)
    damage = TYPE_CHART_MULTIPLIER[move_type][opp_pkm_type] * stab * stage * move_power
    if move_pp == 0:
        return 0.
    return damage

class VGUPolicy(BattlePolicy):
    def requires_encode(self) -> bool:
        return False

    def close(self):
        pass

    def get_action(self, state) -> int: #Gather the state, that is to say active pokemons from both sides)
        my_team = state.teams[0]
        enemy_team = state.teams[1]
        enemy_active = enemy_team.active
        my_pokemon = my_team.active
        max_damage = 0
        best_action = 0
        for j, move in enumerate(my_pokemon.moves):
            damage = damage_estimate(move.type, my_pokemon.type, move.power, enemy_active.type,
                                          my_team.stage[PkmStat.ATTACK], enemy_team.stage[PkmStat.DEFENSE], move.pp)
            # Find Highest Damage!
            if damage > max_damage:
                max_damage = damage
                best_action = j

        return best_action
