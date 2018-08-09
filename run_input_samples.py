#! /usr/bin/python3
# coding: utf-8

from main.solution import Solution
from utils.check_params import (
    check_coordinate, check_direction,
    check_move_str
)

if __name__ == "__main__":
    x = input("请输入一个数字， 标识当前敌军坦克x轴坐标, x=: ")
    x = check_coordinate(x)

    y = input("请输入一个数字， 标识当前敌军坦克y轴坐标, y=: ")
    y = check_coordinate(y)

    direction = input("请输入 'W', 'E', 'S', 'N'中一个方位，标识坦克运动方向, direction=: ")
    direction = check_direction(direction)

    print("您输入的坦克当前数据为: ({x}, {y}) {direction}".format(x=x, y=y, direction=direction))

    move_str = input("请输入一个包含: 'L', 'R', 'M', 'T', 'P'的字符串来标识坦克的移动指令\n如: 'MTMPRPMTMLMRPRMTPLMMTLMRRMP', move_str=: ")
    move_str = check_move_str(move_str)
    
    solute = Solution(x=x, y=y, direction=direction, move_str=move_str)
    position = solute.get_position()
    
    print("\n\n===============================\n")
    print("敌军坦克的坐标为: ", position[0], position[1])
    print("\n===============================\n\n")

    """
    输出: (9, 43), 'E'
    """
