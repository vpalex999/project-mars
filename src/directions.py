from abc import ABC, abstractmethod, abstractproperty

import src.constants as cnst


class AbstractDirection(ABC):

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

    @abstractproperty
    def current(self):
        pass


class BaseDirection(AbstractDirection):

    def __init__(self) -> None:
        self._directions = [cnst.NORTH, cnst.EAST, cnst.SOUTH, cnst.WEST]

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}:"
                f"current direction is '{self.current}'; "
                f"all are '{', '.join(self._directions)}'")

    @property
    def current(self) -> str:
        return self._directions[0]

    def turn_left(self):
        self._directions = [self._directions[-1]] + self._directions[:-1]
        return self

    def turn_right(self):
        self._directions = self._directions[1:] + [self._directions[0]]
        return self
