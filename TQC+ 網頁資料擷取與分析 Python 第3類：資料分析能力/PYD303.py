# 載入 pandas 模組縮寫為 pd
from operator import index
import pandas as pd

#　建構資料
data = [[9, 203674, 13.2, 18894],
       [11.7, 180785, 12.3, 54894],
       [10.1, 127802, 14.7, 18563],
       [11.8, 28604, 14.9, 21963],
       [13.2, 600, 13.1, 900],
       [6.9, 38071, 9.6, 3555],
       [12.1, 35660, 10.6, 9005],
       [12, 15000, 13, 12000],
       [11.7, 48770, 9.1, 14370],
       [9.84, 6100, 11.89, 8980]]
index_ = ["三重市", "台中市", "台北一", "台北二", "台東市", "板橋區", "高雄市", "嘉義市", "鳳山區", "豐原區"]
column_ = ["西瓜價", "西瓜量", "香瓜價", "香瓜量"]

df = pd.DataFrame(data, columns=column_,  index=index_)
print('西瓜與香瓜之拍賣行情價量表')
print(df)
print()  # 使用print分隔


df1 = df.sort_values(by="西瓜價", ascending=False)
print('以西瓜價遞減排序')
print(df1['西瓜價'])
print()  # 使用print分隔

# 計算台北一市場西瓜/香瓜價量的行情並輸出
# df.___["___"]
print('台北一市場的行情')
print(df.loc["台北一"])
print()  # 使用print分隔

index_[0] = "三重區"
df.index = index_
column_[2] = "洋香瓜價"
column_[3] = "洋香瓜量"
df.columns = column_
print('全體市場行情')
print(df)
