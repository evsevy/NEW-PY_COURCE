import pandas as pd

group_data = {"first_range": ['r1','r4','r7','r9','r5','r2','r5','r7','r9'],
              "second_range": ['r10','r40','r70','r90','r50','r20','r50','r70','r90'],
              "account_1": [3,4,7,6,3,9,8,6,7],
              "account_2": [12,34,56,87,65,98,19,76,44],
              "account_3": [9,8,7,6,5,4,3,2,1]}
Group_df = pd.DataFrame(group_data)
print(Group_df)

g_d2=Group_df[["account_1","account_2","account_3" ]].rolling(window=3).mean()
print(g_d2)

Group_df['ewm_30']=Group_df['account_3'].ewm(span=30).mean()
print(Group_df)
