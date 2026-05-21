"""
Developer: Dima
"""

from enum import Enum, auto
import random


class GameStatus( Enum ) :
    PLAY = auto()
    STOP = auto()


class PlayerInputErrorType( Enum ) :
    NOT_NORMAL = auto()
    NORMAL_WRONG_HALF = auto()
    NORMAL_CORRECT_HALF_BUT_NOT_IN_HAND = auto()


class PlayerAction( Enum ) :
    PASS = auto()
    DRAW = auto()


class MoveData :
    def __init__( self ) :
        self.all_player_names = []
        self.names_to_hands : dict[ str, list[ str ] ] = {}
        self.table_bones : list = []
        self.heap : list = []

        self.player_input = ''
        self.bone = ''
        self.last_bone = ''

        self.player_name = ''
        self.player_index = -1
        self.go_to_next_player = True

        self.game_status = GameStatus.PLAY

        self.player_input_error_type = None
        self.player_action = None

        self.drawn_bone = ''


class GameHelper :
    @staticmethod
    def create_all_bones() :
        pass

    @staticmethod
    def get_random_heap_bone( move_data : MoveData ) -> str :
        pass


def init_game( md : MoveData ) :
    pass


def init_move( md : MoveData ) :
    pass


def is_game_over( md : MoveData ) :
    pass


def handle_player_input( md : MoveData ) :
    pass

