from abc import ABC, abstractmethod

import src.constants as cnst


class AbstractDirection(ABC):
    pass


class BaseDirection(AbstractDirection):

    def __init__(self) -> None:
        self._directions = [cnst.NORTH, cnst.EAST, cnst.SOUTH, cnst.WEST]

    @property
    def current(self) -> str:
        return self._directions[0]

    def turn_left(self):
        self._directions = [self._directions[-1]] + self._directions[:-1]
        return self

    def turn_right(self):
        self._directions = self._directions[1:] + [self._directions[0]]
        return self
