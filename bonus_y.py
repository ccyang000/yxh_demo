from loguru import logger
import pandas as pd


def tax_year(num):
    if num <= 0:
        y1 = 0
    elif 0 < num <= 36000:
        y1 = num * 0.03
    elif 36000 < num <= 144000:
        y1 = num * 0.1 - 2520
    elif 144000 < num <= 300000:
        y1 = num * 0.2 - 16920
    elif 300000 < num <= 420000:
        y1 = num * 0.25 - 31920
    elif 420000 < num <= 660000:
        y1 = num * 0.3 - 52920
    elif 660000 < num <= 960000:
        y1 = num * 0.35 - 85920
    elif 960000 < num:
        y1 = num * 0.45 - 181920
    return round(y1, 2)


def tax_bouns(num):
    if num < 0:
        y2 = 0
    elif 0 < num <= 36000:
        y2 = num * 0.03
    elif 36000 < num <= 144000:
        y2 = num * 0.1 - 210
    elif 144000 < num <= 300000:
        y2 = num * 0.2 - 1410
    elif 300000 < num <= 420000:
        y2 = num * 0.25 - 2660
    elif 420000 < num <= 660000:
        y2 = num * 0.3 - 4410
    elif 660000 < num <= 960000:
        y2 = num * 0.35 - 7160
    elif 960000 < num:
        y2 = num * 0.45 - 15160
    return round(y2, 2)


def bonus_plan(total, basic, tunnel_uplimit, leave=False):
    result = []
    channel_tax_rate = 6 / 106
    x4 = tunnel_uplimit
    y4 = round(x4 * channel_tax_rate, 2)

    if leave == False:
        x3 = 0
        y3 = 0

        x1_maybe = [36000 - basic, 144000 - basic, 300000 - basic, 420000 - basic, 660000 - basic, 960000 - basic,
                    960000]
        for x1 in x1_maybe:
            x2 = total - x1 - x4 - x3

            z = x1 + basic
            y1 = tax_year(z)

            y2 = tax_bouns(x2)

            y = y1 + y2 + y3 + y4
            if x1 >= 0 and x2 >= 0 and x3 >= 0 and x4 >= 0:
                result.append([x1, x2, x3, x4, y1, y2, y3, y4, y])

        x2_maybe = [36000, 144000, 300000, 420000, 660000, 960000, 960000]
        for x2 in x2_maybe:
            x1 = total - x2 - x4 - x3

            z = x1 + basic
            y1 = tax_year(z)

            y2 = tax_bouns(x2)

            y = y1 + y2 + y3 + y4
            if x1 >= 0 and x2 >= 0 and x3 >= 0 and x4 >= 0:
                result.append([x1, x2, x3, x4, y1, y2, y3, y4, y])
        # logger.info(result)
        df = pd.DataFrame(result, columns=["??????", "?????????", "????????????", "??????", "???1", "???2", "???3", "???4", "??????"])
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.width', 100)
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = df.sort_values(by="??????")
        # print(df.head(1))
        return df.head(1)


if __name__ == "__main__":
    sxt_path = 'D:\\Python_test\\'
    sxt = pd.read_excel(sxt_path + '???????????????.xlsx', index_col=0)
    sxt_list = sxt.values.tolist()
    result = []
    for i in sxt_list:
        bonus = bonus_plan(i[0], i[1], i[2])
        print(bonus)
        result.append(bonus[:9])

    print(result)

