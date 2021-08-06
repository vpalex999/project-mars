from abc import ABC, abstractmethod
from typing import Any
from src.locations import AbstractLocation
from src.directions import AbstractDirection


class AbstractMap(ABC):

    @abstractmethod
    def cell(self, location: AbstractLocation) -> Any:
        pass

    @abstractmethod
    def has_cell(self, location: AbstractLocation) -> bool:
        pass

    @abstractmethod
    def cell_has_smell(self,
                       location: AbstractLocation,
                       direction: AbstractDirection) -> bool:
        pass

    @abstractmethod
    def cell_has_death_area(self, location: AbstractLocation) -> bool:
        pass

    @abstractmethod
    def cell_mark_smell(self,
                        location: AbstractLocation,
                        direction: AbstractDirection) -> None:
        pass
