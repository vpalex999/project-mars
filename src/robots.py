from abc import ABC, abstractmethod
from src.locations import BaseLocation
from src.directions import BaseDirection


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

    def turn_left(self):
        self._direction.turn_left()
        return self

    def turn_right(self):
        self._direction.turn_right()
        return self

    def forward(self):
        raise NotImplementedError

    @property
    def current_direction(self) -> BaseDirection:
        return self._direction
