#! /usr/bin/python3
# coding: utf-8

def check_coordinate(input_str=None):
    if input_str.isdigit():
        return int(input_str)
    else:
        print("输入的数字不合法！")
        input_str = input("请输入一个数字，标识当前坐标: ")
        return check_coordinate(input_str=input_str)

def check_direction(input_str=None):
    if input_str in ['W', 'S', 'E', 'N']:
        return input_str.upper()
    else:
        print("输入的方位字符不合法！")
        input_str = input("请重新输入一个'W', 'S', 'E', 'N'中的字母，标识当前方位: ")
        return check_direction(input_str=input_str)

def check_move_str(input_str=None):
    input_str.replace(' ', '') 
    for item in input_str:
        if item not in ['L', 'R', 'M', 'T', 'P']:
            print("输入的方位字符不合法！")
            input_str = input("请输入一个包含: 'L', 'R', 'M', 'T', 'P'的字符串来标识坦克的移动指令\n如: 'MTMPRPMTMLMRPRMTPLMMTLMRRMP', move_str=")
            return check_move_str(input_str=input_str)
    return input_str

