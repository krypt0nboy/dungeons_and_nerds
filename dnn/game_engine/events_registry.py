import zope.event.classhandler
from dnn.game_engine.fights.events import FightHasEndedEvent
from dnn.game_engine.characters.events_subscribers import *

zope.event.classhandler.handler(FightHasEndedEvent, fight_has_ended)
