import pandas as pd


sxt_path = 'D:\\Python_test\\'
sxt = pd.read_excel(sxt_path + '净值序列.xlsx', index_col=0)

# print(sxt)

def get_withdraw_num(data, interval= True):
    """
    计算最大回撤
    """

    data = data.sort_index(ascending=True)
    data = data['累计净值']
    temp = pd.DataFrame(columns=['累计净值', '累计最大', '回撤比例'])
    temp['累计净值'] = data
    temp['累计最大'] = temp['累计净值'].expanding().max()
    temp['回撤比例'] = 1 - temp['累计净值'] / temp['累计最大']
    # print(temp)
    withdraw = '%.2f%%' % (100 * temp['回撤比例'].max())

    if interval:
        end_time = temp.index[temp['回撤比例'].values.argmax()]
        end_time = pd.to_datetime(end_time).strftime("%Y-%m-%d")
        start_time = temp.loc[:end_time].sort_values(by='累计净值').index[-1]
        start_time = pd.to_datetime(start_time).strftime("%Y-%m-%d")
        withdraw = (withdraw, start_time, end_time)

    return withdraw

withdraw = get_withdraw_num(sxt)

print("最大回撤为%s, 开始时间是 %s， 结束时间是%s" %withdraw)