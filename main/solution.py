#! /usr/bin/python3
# coding: utf-8


class Solution(object):

    def __init__(self, x, y, direction, move_str):
        self.x = x
        self.y = y
        self.direction = direction
        self.move_str = move_str

    def turn_left(self):
        if self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        else:
            self.direction = 'W'

    def turn_right(self):
        if self.direction == 'W':
            self.direction = 'N'
        elif self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        else:
            self.direction = 'W'

    def move(self):
        if self.direction == 'W':
            self.x -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'N':
            self.y += 1
        else:
            self.y -= 1

    def get_position(self):
        self.move_str = self.move_str.upper()
        for item in self.move_str:
            if item == 'P' or item == "T":
                continue

            if item == "M":
                self.move()
            elif item == "R":
                self.turn_right()
            elif item == "L":
                self.turn_left()
            else:
                pass
        return (self.x, self.y), self.direction
