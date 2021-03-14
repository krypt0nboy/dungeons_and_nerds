"""This file provides with the GameEngine class.

"""
from dnn.game_engine.characters.locks import *
from dnn.game_engine.events_registry import *


class GameEngineBase(object):
    """
    """

    def __init__(self, locks_registry=None):
        self._character_locks_registry = locks_registry or CharacterLocksRegistry()

    def run(self):
        raise NotImplementedError


class ServerLessGameEngine(GameEngineBase):
    """
    """

    def run(self):
        pass


class ServerSideGameEngine(GameEngineBase):
    """
    """

    def __init__(self, **kwargs):
        super(ServerSideGameEngine, self).__init__(**kwargs)
        self._connected_clients = []

    def run(self):
        pass


class ClientSideGameEngine(GameEngineBase):
    """
    """

    def __init__(self, **kwargs):
        super(ClientSideGameEngine, self).__init__(**kwargs)
        self._remote_server = None

    def run(self):
        pass
