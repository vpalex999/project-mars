import pytest

import src.constants as cnst

from src.robots import BaseRobot
from src.locations import BaseLocation


@pytest.fixture
def base_robot():
    return BaseRobot()


def test_init_BaseRobot(base_robot):

    assert isinstance(base_robot, BaseRobot)


def test_robot_start_position(base_robot):
    expected_location = BaseLocation()

    assert base_robot._location == expected_location


@pytest.mark.parametrize(["turn_func", "expected_direction"], [
    (lambda f: f.turn_left(), cnst.WEST),
    (lambda f: f.turn_right(), cnst.EAST),
])
def test_robot_turn_left_or_right(base_robot, turn_func, expected_direction):
    turn_func(base_robot)

    assert base_robot.current_direction.current == expected_direction


def test_robot_forward(base_robot):
    raise NotImplementedError
