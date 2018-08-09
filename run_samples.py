#! /usr/bin/python3
# coding: utf-8

from main.solution import Solution


if __name__ == "__main__":
    sample_str = "MTMPRPMTMLMRPRMTPLMMTLMRRMP"
    solute = Solution(x=11, y=39, direction="W", move_str=sample_str)
    position = solute.get_position()
    
    print("-------------------------\n")
    print("samples: (11, 39) W")
    print("坦克移动信息: ", sample_str)
    print("\n\n==============================\n")
    print("敌军坦克当前坐标为: ", position[0], position[1])
    print("\n==============================\n\n")

    """
    输出: (9, 43), 'E'
    """
