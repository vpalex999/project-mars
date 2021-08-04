import pytest

from src.locations import BaseLocation


class BaseDirection:
    pass


class BasePoint:
    pass


@pytest.fixture
def base_location():
    return BaseLocation()


def test_init_BaseRobot(base_location):

    assert isinstance(base_location, BaseLocation)


def test_equal_locations(base_location):

    assert base_location == BaseLocation(0, 0)


@pytest.mark.parametrize("other_location",
                         [BaseLocation(1, 0),
                          BaseLocation(1, 1),
                          BaseLocation(1, 1)])
def test_is_not_equal_locations(base_location, other_location):

    assert base_location != other_location


def test_set_position(base_location):
    expected_location = BaseLocation(1, 1)
    base_location.set_location(expected_location)

    assert base_location == expected_location