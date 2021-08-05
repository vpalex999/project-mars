from unittest.mock import Mock

import pytest

import src.constants as cnst
from src.robots import BaseRobot
from src.locations import BaseLocation


@pytest.fixture
def fake_map():
    return Mock()


@pytest.fixture
def base_robot(fake_map):
    return BaseRobot(fake_map)


@pytest.fixture
def robot_position_1_1(base_robot):
    return base_robot.forward().turn_right().forward().turn_left()


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

    assert base_robot._direction.current == expected_direction


def test_robot_forward_to_North_by_default(base_robot: BaseRobot):
    base_robot.forward()

    assert base_robot._location == BaseLocation(x=0, y=1)


@pytest.mark.parametrize(["func_turn", "expected_point", "desc"], [
    (lambda robot: robot.turn_left().forward(), (-1, 0), "LEFT WEST and forward"),
    (lambda robot: robot.turn_left().turn_left().forward(),
     (0, -1), "LEFT SOUTH and forward"),
    (lambda robot: robot.turn_left().turn_left().turn_left(
    ).forward(), (1, 0), "LEFT EAST and forward"),
    (lambda robot: robot.turn_right().forward(), (1, 0), "RIGHT EAST and forward"),
    (lambda robot: robot.turn_right().turn_right().forward(),
     (0, -1), "RIGHT SOUTH and forward"),
    (lambda robot: robot.turn_right().turn_right().turn_right(
    ).forward(), (-1, 0), "RIGHT WEST and forward"),

])
def test_robot_forward_in_start_position(base_robot: BaseRobot, func_turn, expected_point, desc):

    func_turn(base_robot)

    assert base_robot._location == BaseLocation(*expected_point)


@pytest.mark.parametrize(["func_turn", "expected_point", "desc"], [
    (lambda robot: robot.turn_left().forward(), (0, 1), "LEFT WEST and forward"),
    (lambda robot: robot.turn_left().turn_left().forward(),
     (1, 0), "LEFT SOUTH and forward"),
    (lambda robot: robot.turn_left().turn_left().turn_left(
    ).forward(), (2, 1), "LEFT EAST and forward"),
    (lambda robot: robot.turn_right().forward(), (2, 1), "RIGHT EAST and forward"),
    (lambda robot: robot.turn_right().turn_right().forward(),
     (1, 0), "RIGHT SOUTH and forward"),
    (lambda robot: robot.turn_right().turn_right().turn_right(
    ).forward(), (0, 1), "RIGHT WEST and forward"),

])
def test_robot_forward_into_map(robot_position_1_1: BaseRobot, func_turn, expected_point, desc):

    func_turn(robot_position_1_1)

    assert robot_position_1_1._location == BaseLocation(*expected_point)
