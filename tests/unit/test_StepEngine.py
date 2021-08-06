import pytest

from src.directions import BaseDirection
from src.locations import BaseLocation
from src.robots import StepEngine


@pytest.mark.parametrize(['set_direction', 'expected_step', 'description'], [
    (lambda f: f, (0, 1), "Step to NORTH"),
    (lambda f: f.turn_left(), (-1, 0), "Step to WEST"),
    (lambda f: f.turn_left().turn_left(), (0, -1), "Step to SOUTH"),
    (lambda f: f.turn_left().turn_left().turn_left(), (1, 0), "Step to EAST"),
])
def test_steps_direction_engine(set_direction, expected_step, description):

    direction = BaseDirection()
    set_direction(direction)

    assert StepEngine.next_step(direction) == BaseLocation(*expected_step)
