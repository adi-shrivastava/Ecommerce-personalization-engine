from sklearn.metrics.pairwise import code_similiarity
import pandas as pd
from db import conn,cursor
query="""select userid,productid,
sum(case
 when eventtype='view' then 1 
 when eventtype ='addtocart' then 3 
 when eventtype='purchased' then 5 
 else 0
 end) 
 as score 
 from events 
 group by userid,productid;"""

df=pd.read_sql(query,conn)
# print(df.head())
matrix=df.pivot_table(
    index="userid",
    columns="productid",
    values="score",
    fill_value=0
)
# print(matrix.head())
# print(matrix.sum(axis=0).sort_values(ascending=False))
# print(matrix.sum(axis=1).sort_values(ascending=False))
# print(matrix.loc[68].sort_values(ascending=False))
# print(matrix.stack().sort_values(ascending=False).head(10))