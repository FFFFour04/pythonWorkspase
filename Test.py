import tushare as ts
import pandas as pd
from util import PolicyUtil

# 通过股票代码获取股票数据,这里没有指定开始及结束日期
df = ts.get_k_data('000651','2020-04-13','2020-04-15','D')
df = ts.get_k_data("300104")

# 查看前十条数据
df.head()

# 查看后十条数据
df.tail()

# 将数据的index转换成date字段对应的日期
df.index = pd.to_datetime(df.date)

# 将多余的date字段删除
df.drop("date", inplace=True, axis=1)

print(df)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 取第一条数据
print(df[0:1])
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 取open列的数据
print(df['open'])
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 计算5,15,50日的移动平均线, MA5, MA15, MA50
days = [5, 15, 50]
for ma in days:
    column_name = "MA{}".format(ma)
    # 增加,15,50日移动平均线的列
    df[column_name] = df.close.rolling(ma).mean()

# 计算浮动比例
df["pchange"] = df.close.pct_change()
# 计算浮动点数
df["change"] = df.close.diff()

# plot函数，画图工具
# df[["close", "MA5", "MA15", "MA50"]].plot(figsiz=(10,18))

pu = PolicyUtil('1234')