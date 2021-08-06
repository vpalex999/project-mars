import pytest

from unittest.mock import Mock

from src.robots import RobotChappiV1
from src.locations import BaseLocation
from src.maps import AbstractMap


@pytest.fixture
def fake_map():
    return Mock(AbstractMap)


@pytest.fixture
def chappi_v1(fake_map):
    return RobotChappiV1(fake_map)


def test_init(fake_map):

    robot = RobotChappiV1(fake_map)

    assert isinstance(robot, RobotChappiV1)


def set_chappi(robot,
               cell_has_smell=False,
               cell_has_death_area=False,
               has_cell=True,
               alive=True
               ):
    robot._map.cell_has_smell.return_value = cell_has_smell
    robot._map.cell_has_death_area.return_value = cell_has_death_area
    robot._map.has_cell.return_value = has_cell
    robot._alive = alive


@pytest.mark.parametrize(
    ['robot_attr', 'expected_prev_location',
        'expected_location', 'expected_alive', 'description'],
    [
        (dict(), (0, 0), (0, 1), True, "forward"),
        (dict(alive=False), (0, 0), (0, 0), False, "forward if Robot was death"),
        (dict(cell_has_smell=True), (0, 0), (0, 0),
         True, "forward if Robot has smell"),
        (dict(has_cell=False), (0, 0), (0, 1), False, "forward out boundary"),
        (dict(cell_has_death_area=True), (0, 0),
         (0, 1), False, "forward into death area"),
    ])
def test_forward_on_map(chappi_v1: RobotChappiV1,
                        robot_attr,
                        expected_prev_location,
                        expected_location,
                        expected_alive,
                        description):

    set_chappi(chappi_v1, **robot_attr)

    chappi_v1.forward()

    assert chappi_v1._prev_location == BaseLocation(*expected_prev_location)
    assert chappi_v1._location == BaseLocation(*expected_location)
    assert chappi_v1._alive == expected_alive


def test__location_has_smell(chappi_v1: RobotChappiV1):
    chappi_v1._map.cell_has_smell.return_value = True
    assert chappi_v1._location_has_smell() is True


def test__location_is_out_boundary(chappi_v1: RobotChappiV1):
    chappi_v1._map.has_cell.return_value = False
    assert chappi_v1._location_is_out_boundary() is True


def test__location_is_death_area(chappi_v1: RobotChappiV1):
    chappi_v1._map.cell_has_death_area.return_value = True
    assert chappi_v1._location_is_death_area() is True


def test_go_death(chappi_v1: RobotChappiV1):
    chappi_v1._go_death()

    chappi_v1._map.cell_mark_smell.assert_called_once()
    assert chappi_v1._alive is False
