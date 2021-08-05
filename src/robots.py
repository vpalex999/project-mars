from abc import ABC, abstractmethod


import src.constants as cnst
from src.locations import BaseLocation
from src.directions import BaseDirection
from src.directions import AbstractDirection
from src.maps import AbstractMap



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

    def __init__(self, map: AbstractMap) -> None:
        self._map = map
        self._alive: bool = True
        self._location = BaseLocation()
        self._direction = BaseDirection()

    @property
    def is_alive(self) -> bool:
        return self._alive

    def turn_left(self):
        self._direction.turn_left()
        return self

    def turn_right(self):
        self._direction.turn_right()
        return self

    def forward(self):
        step_directions = {
            cnst.NORTH: BaseLocation(x=0, y=1),
            cnst.EAST: BaseLocation(x=1, y=0),
            cnst.SOUTH: BaseLocation(x=0, y=-1),
            cnst.WEST: BaseLocation(x=-1, y=0),
        }

        new_location = self._location.add_location(step_directions[self._direction.current])
        self._location.set_location(new_location)

        return self


class RobotChappi(BaseRobot):

    @property
    def current_direction(self) -> AbstractDirection:
        return self._direction
