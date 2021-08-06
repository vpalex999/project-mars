from abc import ABC, abstractmethod


class AbstractLocation(ABC):

    @abstractmethod
    def set_location(self, location: object) -> None:
        pass


class BaseLocation(AbstractLocation):

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y

    def __eq__(self, location: object) -> bool:
        return self._x == location._x and \
            self._y == location._y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}:x={self._x};y={self._y}"

    def set_location(self, location) -> None:
        self._x = location._x
        self._y = location._y

    def join(self, location):
        new_location = BaseLocation(
            self._x + location._x,
            self._y + location._y)

        return new_location
