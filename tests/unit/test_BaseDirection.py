import pytest

import src.constants as cnst
from src.directions import BaseDirection


@pytest.fixture
def base_direction():
    return BaseDirection()


def test_init_BaseDirection(base_direction):
    assert isinstance(base_direction, BaseDirection)


def test_current_direction_is(base_direction):
    assert base_direction.current == cnst.NORTH


@pytest.mark.parametrize(["turn_func", "expected_direction"], [
    # turn_left
    (lambda f: f.turn_left(), cnst.WEST),
    (lambda f: f.turn_left().turn_left(), cnst.SOUTH),
    (lambda f: f.turn_left().turn_left().turn_left(), cnst.EAST),
    (lambda f: f.turn_left().turn_left().turn_left().turn_left(), cnst.NORTH),
    (lambda f: f.turn_left().turn_left().turn_left().turn_left().turn_left(), cnst.WEST),
    # turn_right()
    (lambda f: f.turn_right(), cnst.EAST),
    (lambda f: f.turn_right().turn_right(), cnst.SOUTH),
    (lambda f: f.turn_right().turn_right().turn_right(), cnst.WEST),
    (lambda f: f.turn_right().turn_right().turn_right().turn_right(), cnst.NORTH),
    (lambda f: f.turn_right().turn_right().turn_right().turn_right().turn_right(), cnst.EAST),
    # any combinations
    (lambda f: f.turn_left().turn_right(), cnst.NORTH),
    (lambda f: f.turn_left().turn_left().turn_right(), cnst.WEST),
    (lambda f: f.turn_left().turn_right().turn_left(), cnst.WEST),
    (lambda f: f.turn_left().turn_right().turn_left().turn_right().turn_right(), cnst.EAST),
]
)
def test_turn_direction(base_direction, turn_func, expected_direction):

    turn_func(base_direction)

    assert base_direction.current == expected_direction
