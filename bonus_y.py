from loguru import logger
import pandas as pd


def bonus(total, basic, uplimit, leave=False, ):
    result = []
    channel_tax_rate = 6 / 106
    x4 = uplimit
    y4 = x4 * channel_tax_rate

    if leave == False:
        x3 = 0
        y3 = 0

        x1_maybe = [36000 - basic, 144000 - basic, 300000 - basic, 420000 - basic, 660000 - basic, 960000 - basic, 960000]
        for x1 in x1_maybe:
            x2 = total - x1 - x4 - x3

            z = x1 + basic
            if z <= 0:
                y1 = 0
            elif 0 < z <= 36000:
                y1 = z * 0.03
            elif 36000 < z <= 144000:
                y1 = z * 0.1 - 2520
            elif 144000 < z <= 300000:
                y1 = z * 0.2- 16920
            elif 300000 < z <= 420000:
                y1 = z * 0.25 - 31920
            elif 420000 < z <= 660000:
                y1 = z * 0.3 -52920
            elif 660000 < z <= 960000:
                y1 = z * 0.35 -85920
            elif 960000 < z:
                y1 = z * 0.45 -181920


            if 0 < x2 <= 36000:
                y2 = x2 * 0.03
            elif 36000 < x2 <= 144000:
                y2 = x2 * 0.1 - 210
            elif 144000 < x2 <= 300000:
                y2 = x2 * 0.2- 1410
            elif 300000 < x2 <= 420000:
                y2 = x2 * 0.25- 2660
            elif 420000 < x2 <= 660000:
                y2 = x2 * 0.3 - 4410
            elif 660000 < x2 <= 960000:
                y2 = x2 * 0.35- 7160
            elif 960000 < x2:
                y2 = x2 * 0.45 - 15160

            y = y1 + y2 + y3 + y4
            if x1 >= 0 and x2 >= 0 and x3 >= 0 and x4 >= 0:
                result.append([x1, x2, x3, x4, y1, y2, y3, y4, y])

        x2_maybe = [36000, 144000, 300000, 420000, 660000, 960000, 960000]
        for x2 in x2_maybe:
            x1 = total - x2 - x4 - x3

            z = x1 + basic
            if z <= 0:
                y1 = 0
            elif 0 < z <= 36000:
                y1 = z * 0.03
            elif 36000 < z <= 144000:
                y1 = z * 0.1 - 2520
            elif 144000 < z <= 300000:
                y1 = z * 0.2 - 16920
            elif 300000 < z <= 420000:
                y1 = z * 0.25 - 31920
            elif 420000 < z <= 660000:
                y1 = z * 0.3 - 52920
            elif 660000 < z <= 960000:
                y1 = z * 0.35 - 85920
            elif 960000 < z:
                y1 = z * 0.45 - 181920

            if 0 < x2 <= 36000:
                y2 = x2 * 0.03
            elif 36000 < x2 <= 144000:
                y2 = x2 * 0.1 - 210
            elif 144000 < x2 <= 300000:
                y2 = x2 * 0.2 - 1410
            elif 300000 < x2 <= 420000:
                y2 = x2 * 0.25 - 2660
            elif 420000 < x2 <= 660000:
                y2 = x2 * 0.3 - 4410
            elif 660000 < x2 <= 960000:
                y2 = x2 * 0.35 - 7160
            elif 960000 < x2:
                y2 = x2 * 0.45 - 15160

            y = y1 + y2 + y3 + y4
            if x1 >= 0 and x2 >= 0 and x3 >= 0 and x4 >= 0:
                result.append([x1, x2, x3, x4, y1, y2, y3, y4, y])
        logger.info(result)


bonus(1000000, 600000, 200000)
