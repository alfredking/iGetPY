from jqdata import *
import pandas as pd

auth('18867101271','157268ak')
q  = query(jy.LC_IndexDerivative.TradingDay,
    jy.LC_IndexDerivative.PB_LF,

          ).filter(jy.LC_IndexDerivative.IndexCode == "4978",
                                        jy.LC_IndexDerivative.TradingDay<='2020-04-17'
                                        ).order_by(
    jy.LC_IndexDerivative.TradingDay)
df  = jy.run_query(q).set_index("TradingDay")
df.index = pd.to_datetime(df.index)
price_df =  get_price("000905.XSHG",end_date='2020-04-17',start_date=df.index[0],fields='close').close

def max_down_num(x): #计算回撤超过20%的天数
    returns = (x - x[0])/x[0]
    return (returns<-0.2).sum()

df['max_down_count'] = price_df.rolling(252).apply(max_down_num,raw=True).shift(-252)
df['max_down_count2'] = price_df.rolling(252*2).apply(max_down_num,raw=True).shift(-252*2)

df['is_in_limit']  = (df.PB_LF< df.PB_LF.iloc[-1]+0.3)&(df.PB_LF>df.PB_LF.iloc[-1]-0.3)