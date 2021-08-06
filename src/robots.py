from abc import ABC, abstractmethod


import src.constants as cnst
from src.locations import BaseLocation
from src.directions import BaseDirection
from src.maps import AbstractMap


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
        self._prev_location = BaseLocation()
        self._direction = BaseDirection()

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


class RobotChappiV1(BaseRobot):

    def __init__(self, map: AbstractMap) -> None:
        super().__init__()
        self._map = map
        self._alive = True

    def forward(self):
        if not self._alive or self._location_has_smell():
            return self

        super().forward()

        if self._location_is_out_boundary() or self._location_is_death_area():
            self._go_death()
        return self

    def _location_has_smell(self) -> bool:
        return self._map.cell_has_smell(self._location, self._direction)

    def _location_is_out_boundary(self) -> bool:
        return not self._map.has_cell(self._location)

    def _location_is_death_area(self):
        return self._map.cell_has_death_area(self._location)

    def _go_death(self):
        self._mark_cell_smell()
        self._alive = False

    def _mark_cell_smell(self):
        self._map.cell_mark_smell(self._location, self._direction)
