from abc import ABC, abstractmethod


import src.constants as cnst
from src.locations import BaseLocation
from src.directions import BaseDirection


class StepEngine:
    steps_map = {
        cnst.NORTH: BaseLocation(x=0, y=1),
        cnst.EAST: BaseLocation(x=1, y=0),
        cnst.SOUTH: BaseLocation(x=0, y=-1),
        cnst.WEST: BaseLocation(x=-1, y=0),
    }

    @staticmethod
    def next_step(direction: BaseDirection) -> BaseLocation:
        return StepEngine.steps_map[direction.current]


class AbstractRobot(ABC):

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

    @abstractmethod
    def forward(self):
        pass


class BaseRobot(AbstractRobot):

    def __init__(self) -> None:
        self._location = BaseLocation()
        self._direction = BaseDirection()
        self._prev_location = None

    def turn_left(self):
        self._direction.turn_left()
        return self

    def turn_right(self):
        self._direction.turn_right()
        return self

    def forward(self):
        next_step = StepEngine.next_step(self._direction)
        new_location = self._location.join(next_step)

        self._prev_location, self._location = self._location, new_location

        return self
