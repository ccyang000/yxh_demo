"""
x1 + x2 + x3 = 10
x1 = 2 * x2
xi是自然数，求所有的x1,x2,x3三元组
"""
from loguru import logger

res = []
for x1 in range(11):
    for x2 in range(11):
        x3 = 10 - x1 - x2
        if (x1 == 2 * x2) and (x3 > 0):
            res.append([x1, x2, x3])

logger.info(res)

