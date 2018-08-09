# 题目描述
```
我军: 
    关键高地坐标设定为: (x=0, y=0)
    规定: 
        向东增加100米， x += 1
        向北增加100米, y += 1

敌军:
    坦克运动: (L, R, M)
    说明:
        L: 向左转向
        R: 向右转向
        M: 直线前进100米
        T: 时间同步
        P: 位置校准

侦查:
    坦克坐标: (P, Q)
    坦克前进方向: W, E, N, S
    坦克接收信号实时同步

实例:
    坦克坐标: (11, 39)
    运行方向: W
    接收信号: MTMPRPMTMLMRPRMTPLMMTLMRRMP

实例输出:
    坦克坐标: (9, 43)
    运行方向: E
```

# 解体思路
```
1. T，P为额外参数，未参与计算坐标，可不考虑
2. 坐标S,W,N,E与L, R之间的关系已知
3. 当方位为S时，执行Move操作，则y坐标-1, 其它方位执行Move操作同理
```

# 目录结构
```
├── README.md
├── conftest.py
├── main
│   ├── __init__.py
│   └── solution.py
├── pytest_report.txt
├── pytest_report_log.txt
├── requirements.txt
├── run_input_samples.py
├── run_samples.py
├── setup.cfg
├── tests
│   ├── reportlog.txt
│   └── test_solution.py
├── utils
│   ├── __init__.py
│   └── check_params.py
├── 图片1.jpg
├── 图片2.jpg
└── 题目介绍.jpg
```

# 运行命令
```
# 在tuo_tian_su_dai/目录下运行:

>>> py.test

# 得到测试报告如: pytest_report.txt中的内容
```

```
# 在tuo_tian_su_dai/目录下运行:

>>> python3 run_samples.py

# 得到如[图片1.jpg]的结果
```

```
# 在tuo_tian_su_dai/目录下运行:

>>> python3 run_input_samples.py
>>> # 根据提示输入相应数据

# 得到如[图片2.jpg]的结果
```
