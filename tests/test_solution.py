#! /usr/bin/python3
# coding: utf-8

from main.solution import Solution


class TestSolution(object):

    def test_turn_left(self):
        solute = Solution(x=1, y=1, direction='E', move_str="LRM")
        solute.turn_left()
        assert solute.direction == 'N'

    def test_turn_right(self):
        solute = Solution(x=1, y=1, direction='E', move_str="LRM")
        solute.turn_right()
        assert solute.direction == 'S'

    def test_get_position(self):
        solute = Solution(x=1, y=1, direction='E', move_str="RM")
        solute.get_position()
        assert solute.direction == 'S'
        assert solute.x == 1
        assert solute.y == 0

